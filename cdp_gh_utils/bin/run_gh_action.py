#!/usr/bin/env python

import argparse
import logging
import sys
import traceback

from cdp_gh_utils import actions, argparse_utils

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Args(argparse.Namespace):
    def __init__(self) -> None:
        self.__parse()

    def __parse(self) -> None:
        p = argparse.ArgumentParser(
            prog="run-gh-action",
            description="Run a GitHub Action.",
        )
        p.add_argument(
            "repo",
            type=str,
            help=(
                "The organization and name of the GitHub repository. "
                "i.e. 'evamaxfield/cdp-gh-utils'"
            ),
        )
        p.add_argument(
            "workflow_file_name",
            type=str,
            help=("The name of the workflow file to run. " "i.e. 'ci.yml'"),
        )
        p.add_argument(
            "--watch",
            action="store_true",
            help="After starting the worklow run, should we watch the progress.",
        )
        p.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what command would be run.",
        )
        p.add_argument(
            "-k",
            "--kwargs",
            nargs="*",
            action=argparse_utils.ParseKwargs,
            help="A list of kwargs with `{name}={value}` format.",
        )
        p.add_argument(
            "--debug",
            dest="debug",
            action="store_true",
            help="Run with debug logging.",
        )
        p.parse_args(namespace=self)


def main() -> None:
    # Get args
    args = Args()

    # Determine log level
    if args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    # Setup logging
    logging.basicConfig(
        level=log_level,
        format="[%(levelname)4s: %(module)s:%(lineno)4s %(asctime)s] %(message)s",
    )

    # Process
    try:
        result = actions.run(
            repo=args.repo,
            workflow_file_name=args.workflow_file_name,
            parameters=args.kwargs,
            watch=args.watch,
            dry_run=args.dry_run,
        )
        log.info(f"Workflow resulted in: '{result.state}'")
    except Exception as e:
        log.error("=============================================")
        log.error("\n\n" + traceback.format_exc())
        log.error("=============================================")
        log.error("\n\n" + str(e) + "\n")
        log.error("=============================================")
        sys.exit(1)


###############################################################################
# Allow caller to directly run this module (usually in development scenarios)

if __name__ == "__main__":
    main()
