#!/usr/bin/env python

from __future__ import annotations

import argparse
from collections.abc import Iterable
from typing import Any, Sequence

###############################################################################


class ParseKwargs(argparse.Action):
    """
    Parse keyword arguments from CLI to dictionary.

    Credit:
    https://sumit-ghosh.com/articles/parsing-dictionary-key-value-pairs-kwargs-argparse-python/

    Examples
    --------
    ```
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--kwargs', nargs='*', action=ParseKwargs)
    args = parser.parse_args()
    ```
    """

    def __call__(
        self: ParseKwargs,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None:
        """Call the dictionary parser."""
        setattr(namespace, self.dest, {})
        if isinstance(values, Iterable):
            for value in values:
                key, value = value.split("=")
                getattr(namespace, self.dest)[key] = value
