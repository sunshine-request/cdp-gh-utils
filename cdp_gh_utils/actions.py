#!/usr/bin/env python

from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass

###############################################################################

log = logging.getLogger(__name__)

###############################################################################

GH_ACTIONS_COMMAND_TEMPLATE = (
    "gh workflow run " "--repo {repo} " "{workflow_file_name} " "{parameters}"
)

###############################################################################


@dataclass
class RunResult:
    state: str
    command: str


def run(
    repo: str,
    workflow_file_name: str,
    parameters: dict[str, str] | None = None,
    watch: bool = False,
    dry_run: bool = False,
) -> RunResult:
    # If there are parameters, compile them
    if parameters:
        compiled_parameters = " ".join([f"-f {k}={v}" for k, v in parameters.items()])
    else:
        compiled_parameters = ""

    # Fill the full command
    filled_command = GH_ACTIONS_COMMAND_TEMPLATE.format(
        repo=repo,
        workflow_file_name=workflow_file_name,
        parameters=compiled_parameters,
    ).strip()

    # Handle dry run
    if dry_run:
        log.info(f"Would have submitted job: '{filled_command}'")
        return RunResult(
            state="Dry run success",
            command=filled_command,
        )

    # Actual run
    try:
        proc_resp = subprocess.run(
            filled_command.split(" "),
            check=True,
        )
        log.info(f"Submitted job: '{filled_command}'")
        print(proc_resp)

    except subprocess.CalledProcessError as e:
        log.error(f"Failed during '{filled_command}' (watch={watch})")
        log.error(e)
        return RunResult(
            state=f"Error: {e}",
            command=filled_command,
        )

    return RunResult(
        state="Job submit sucess",
        command=filled_command,
    )
