import collections
import concurrent.futures
import enum
import functools
import itertools
import json
import logging
import os
import sys
import textwrap
import threading
import time
from typing import (
    Any,
    Deque,
    List,
    Optional,
    cast,
)


if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from kintro.decisions import DECISION_TYPES

import click
from click_option_group import (
    AllOptionGroup,
    optgroup,
)
import enlighten
import more_itertools
import plexapi.library
import plexapi.server
from plexapi.video import Episode


class AppObj(TypedDict):
    plex: plexapi.server.PlexServer
    logger: logging.Logger
    debug: bool


@enum.unique
class LibType(enum.Enum):
    Episode = "episode"
    Show = "show"


@enum.unique
class Analyze(enum.Enum):
    NoAnalyze = 0
    AnalyzeIfIntroMissing = 1
    ForceAnalyze = 2


def to_analyze(app_obj: AppObj, *, analyze_if_intro_missing: bool, force_analyze: bool) -> Analyze:
    if force_analyze:
        if analyze_if_intro_missing:
            app_obj["logger"].warning("--force-analyze overrides --analyze-if-intro-missing")
        return Analyze.ForceAnalyze
    if analyze_if_intro_missing:
        return Analyze.AnalyzeIfIntroMissing
    return Analyze.NoAnalyze


@click.command(context_settings={"show_default": True})
@click.option("--library", required=True, default="TV Shows", help="Plex library to operate on")
@click.option(
    "--edit",
    type=click.Choice(["cut", "mute", "scene", "commercial"]),
    default="scene",
    help="""\b
    cut: Makes it so the intro is completely gone
    mute: Makes it so the intro's audio is muted
    scene: Makes it so the nextscene action skips to the end of the intro
    commercial: Makes it so the intro is skipped once (like cut), but is then seekable after
    """,
)
@click.option(
    "--dry-run",
    default=False,
    is_flag=True,
    help="Logs the .edl files kintro will write without writing them",
)
@click.option(
    "--libtype",
    default=LibType.Episode.value,
    type=click.Choice([x.name for x in LibType], case_sensitive=False),
    help="type of search to do",
)
@click.option("--filter-json", default=None, help="json representing plex filters")
@optgroup.group(
    "Find and Replace",
    cls=AllOptionGroup,
    help="Find and Replace options for fixing file paths (useful for plex servers running in containers)",
)
@optgroup.option("--find-path", help="Find string")
@optgroup.option("--replace-path", type=click.Path(exists=True), help="Replace directory")
@click.option("--max-workers", default=4, help="Max Number of workers to process episodes")
@click.option("--worker-batch-size", default=10, help="Chunk of work to hand off to each worker")
@click.option(
    "--analyze-if-intro-missing",
    default=False,
    is_flag=True,
    help=textwrap.dedent(
        """\
        (Advanced) Perform analyze on episode if intro is missing (potentially expensive)
            Take care with this flag and --max-workers or unfiltered libraries
    """
    ),
)
@click.option(
    "--force-analyze",
    default=False,
    is_flag=True,
    help=textwrap.dedent(
        """\
        (Advanced) Perform analyze on episode (Overrides --analyze-if-intro-missing) (potentially very expensive)
            Take care with this flag and --max-workers or unfiltered libraries
    """
    ),
)
@click.pass_context
def sync(
    ctx: click.Context,
    library: str,
    edit: str,
    dry_run: bool,
    libtype: str,
    filter_json: Optional[str],
    find_path: Optional[str],
    replace_path: Optional[str],
    max_workers: int,
    worker_batch_size: int,
    analyze_if_intro_missing: bool,
    force_analyze: bool,
) -> None:
    app_obj: AppObj = ctx.obj
    return sync_internal(
        app_obj=app_obj,
        library=library,
        edit=edit,
        dry_run=dry_run,
        libtype=libtype,
        filter_json=filter_json,
        find_path=find_path,
        replace_path=replace_path,
        max_workers=max_workers,
        worker_batch_size=worker_batch_size,
        analyze_if_intro_missing=analyze_if_intro_missing,
        force_analyze=force_analyze,
    )


def sync_internal(
    app_obj: AppObj,
    library: str,
    edit: str,
    dry_run: bool,
    libtype: str,
    filter_json: Optional[str],
    find_path: Optional[str],
    replace_path: Optional[str],
    max_workers: int,
    worker_batch_size: int,
    analyze_if_intro_missing: bool,
    force_analyze: bool,
) -> None:
    app_obj["logger"].info("Starting sync process")

    plex: plexapi.server.PlexServer = app_obj["plex"]
    libtype_val: LibType = LibType(libtype.lower())
    edit_val = DECISION_TYPES[edit]

    should_analyze = to_analyze(app_obj, analyze_if_intro_missing=analyze_if_intro_missing, force_analyze=force_analyze)

    more_search = {"filters": json.loads(filter_json)} if filter_json is not None else {}
    shows_section = cast(plexapi.library.ShowSection, plex.library.section(library))

    tv: List[Episode] = {  # type: ignore[no-untyped-call]
        LibType.Episode: lambda: shows_section.search(**more_search, libtype="episode"),
        LibType.Show: lambda: list(
            itertools.chain(
                *(
                    show.episodes()
                    for show in shows_section.search(
                        **more_search,
                        libtype="show",
                    )
                ),
            )
        ),
    }[libtype_val]()

    with enlighten.get_manager() as manager:
        pbar = manager.counter(total=len(tv), desc="episodes:", unit="episodes", color="green")

        if max_workers == 1:
            for episode in (
                tv
                if worker_batch_size == 1
                else itertools.chain.from_iterable(more_itertools.ichunked(tv, worker_batch_size))
            ):
                handle_episode(
                    app_obj=app_obj,
                    episode=episode,
                    edit=edit_val,
                    find_path=find_path,
                    replace_path=replace_path,
                    dry_run=dry_run,
                    pbar=pbar,
                    should_analyze=should_analyze,
                )
        else:
            # Break the TV into yielding iterator chunks for batch processing
            tv_chunked = more_itertools.ichunked(tv, worker_batch_size)

            # Queues for interthread batches and results
            batch_queue: Deque[List[Episode]] = collections.deque()
            results: Deque[List[str]] = collections.deque()
            # Events controlling if processing threads are allowed to start or stop
            start_event = threading.Event()
            stop_event = threading.Event()

            def submit() -> None:
                app_obj["logger"].debug("Putting all episodes in batched queue")
                for episodes in tv_chunked:
                    app_obj["logger"].debug(f"Putting chunk of episodes in batched queue")
                    batch_queue.append(list(episodes))
                    start_event.set()
                    time.sleep(0.01)
                start_event.set()
                app_obj["logger"].debug("Sending stop event")
                stop_event.set()

            # Start the submitter in a background thread
            app_obj["logger"].debug(f"Starting submitter background thread")
            submitter = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            submitter_res = submitter.submit(submit)

            app_obj["logger"].debug(
                f"Starting processing pool with max #{max_workers} workers and batch size {worker_batch_size}"
            )
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

            # Bind all the non varying args for the worker function
            handle_eps = functools.partial(
                handle_episodes,
                app_obj=app_obj,
                edit=edit_val,
                find_path=find_path,
                replace_path=replace_path,
                dry_run=dry_run,
                episodes_source=batch_queue,
                results_sink=results,
                start_event=start_event,
                stop_event=stop_event,
                pbar=pbar,
                should_analyze=should_analyze,
            )

            app_obj["logger"].debug(f"Starting worker fucntions on pool threads (#{max_workers})")
            res = executor.map(
                handle_eps,
                [x for x in range(0, max_workers)],
            )

            app_obj["logger"].debug("Requesting the submitter be destroyed")
            submitter.shutdown()
            app_obj["logger"].debug("Requesting the worker pool be destroyed")
            executor.shutdown()

            if app_obj["debug"]:
                try:
                    for r in res:
                        app_obj["logger"].debug(f"Worker thread launch result: {r}")
                except Exception as e:
                    app_obj["logger"].exception(f"Error while checking worker thread status {e}")

                try:
                    app_obj["logger"].debug(f"Submitter thread status {submitter_res.result()}")
                except Exception as e:
                    app_obj["logger"].exception(f"Error while checking submitter thread status {e}")

                while True:
                    app_obj["logger"].debug("Looping on results")
                    try:
                        result = results.pop()
                        if len(result) > 0:
                            app_obj["logger"].debug(result)
                    except IndexError:
                        break


def handle_episodes(
    _ix: int,
    *,
    episodes_source: Deque[List[Episode]],
    results_sink: Deque[List[str]],
    start_event: threading.Event,
    stop_event: threading.Event,
    app_obj: AppObj,
    edit: DECISION_TYPES,
    find_path: Optional[str],
    replace_path: Optional[str],
    dry_run: bool,
    pbar: Any,
    should_analyze: Analyze,
) -> None:
    app_obj["logger"].info(f"Starting a episodes thread {threading.current_thread().name}")
    app_obj["logger"].debug(f"Waiting for start event on thread {threading.current_thread().name}")
    start_event.wait()
    app_obj["logger"].debug(f"Done Waiting for start event on thread {threading.current_thread().name}")
    while True:
        try:
            episodes = list(episodes_source.pop())
            app_obj["logger"].debug(
                f"Starting a batch of {len(episodes)} episodes on thread {threading.current_thread().name}"
            )
            for episode in episodes:
                results_sink.append(
                    handle_episode(
                        app_obj=app_obj,
                        episode=episode,
                        edit=edit,
                        find_path=find_path,
                        replace_path=replace_path,
                        dry_run=dry_run,
                        pbar=pbar,
                        should_analyze=should_analyze,
                    ),
                )
        except IndexError as _e:
            if stop_event.is_set():
                break
            app_obj["logger"].debug(
                f"Nothing in queue to process in {threading.current_thread().name} continuing in 1 second"
            )
            time.sleep(1)
        except Exception as e:
            app_obj["logger"].warning(
                f"Exception {e} in {threading.current_thread().name} while handling batch of episodes, continuing..."
            )
            continue
    return None


def handle_episode(
    app_obj: AppObj,
    episode: Episode,
    edit: DECISION_TYPES,
    find_path: Optional[str],
    replace_path: Optional[str],
    dry_run: bool,
    pbar: Any,
    should_analyze: Analyze,
) -> List[str]:
    files_to_modify = []

    app_obj["logger"].debug(
        f'Checking for intro marker show="{episode.grandparentTitle}"'
        f' season={episode.seasonNumber} episode={episode.episodeNumber} title="{episode.title}"',
    )

    def may_analyze(cond: bool, message: str) -> None:
        if cond:
            app_obj["logger"].info(
                f'{message}: show="{episode.grandparentTitle}"'
                f' season={episode.seasonNumber} episode={episode.episodeNumber} title="{episode.title}"'
            )
            episode.analyze()
            episode.reload()

    try:
        may_analyze(should_analyze == Analyze.ForceAnalyze, "Force analyzing")
        may_analyze(
            not episode.hasIntroMarker and should_analyze == Analyze.AnalyzeIfIntroMissing, "Missing intro, analyzing"
        )
        # This call is EXTREMELY expensive, do not prefilter on it (this lets threads bear the weight)
        if episode.hasIntroMarker and len([marker for marker in episode.markers if marker.type == "intro"]) > 0:
            # multiple markers can exist for a file. only want type intro,
            # but it's possible there could be more than one intro
            for marker in episode.markers:
                if marker.type == "intro":
                    start = marker.start / 1000
                    end = marker.end / 1000
                    # build the content for the file
                    intro_entry = f"{start} {end} {edit.value}"
                    # plex can expose multiple locations for a video/episode, so we should
                    # iterate through them and write an .edl file for each
                    for location in episode.locations:
                        file_path = os.path.splitext(location)[0] + ".edl"
                        # if we're running in a container or otherwise need to fix the path
                        if find_path:
                            file_path = file_path.replace(find_path, replace_path)
                        if not dry_run:
                            with open(file_path, "w") as writer:
                                writer.write(intro_entry)

                        files_to_modify.append(file_path)

                        app_obj["logger"].info(
                            f'show="{episode.grandparentTitle}"'
                            f' season={episode.seasonNumber} episode={episode.episodeNumber} title="{episode.title}"'
                            f' location="{episode.locations} start={start} end={end} file="{file_path}"',
                        )
        # we should log when we don't find an intro
        else:
            app_obj["logger"].info(
                f'show="{episode.grandparentTitle}"'
                f' season={episode.seasonNumber} episode={episode.episodeNumber} title="{episode.title}"'
                f' location="{episode.locations} msg="No intro markers found"',
            )
    except Exception as e:
        app_obj["logger"].warning(
            f"Exception {e} in {threading.current_thread().name} while handling and episode, continuing..."
        )
    # always update the progress bar
    finally:
        pbar.update()

    return files_to_modify
