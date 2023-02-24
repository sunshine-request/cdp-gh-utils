#!/usr/bin/env python

import argparse

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

    def __call__(self, parser, namespace, values, option_string=None):
        """Call the dictionary parser."""
        setattr(namespace, self.dest, {})
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value