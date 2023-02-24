#!/usr/bin/env python

from __future__ import annotations

import pytest

from cdp_gh_utils import actions


###############################################################################


@pytest.mark.parametrize(
    "repo, workflow_file_name, parameters, dry_run, watch, expected",
    [
        (
            "doesnt/matter",
            "fake.yml",
            None,
            True,
            False,
            actions.RunResult(
                state="Dry run success",
                command="gh workflow run --repo doesnt/matter fake.yml"
            )
        ),
        (
            "doesnt/matter",
            "fake.yml",
            {"hello": "world", "a": "b"},
            True,
            False,
            actions.RunResult(
                state="Dry run success",
                command=(
                    "gh workflow run --repo doesnt/matter fake.yml "
                    "-f hello=world -f a=b"
                )
            ),
        ),
    ],
)
def test_run(
    repo: str,
    workflow_file_name: str,
    parameters: dict[str, str] | None,
    dry_run: bool,
    watch: bool,
    expected: actions.RunResult,
) -> None:
    actual = actions.run(
        repo=repo,
        workflow_file_name=workflow_file_name,
        parameters=parameters,
        dry_run=dry_run,
        watch=watch,
    )
    assert actual.state == expected.state
    assert actual.command == expected.command
