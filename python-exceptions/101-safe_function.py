#!/usr/bin/python3
"""Module for safe_function function."""
import sys


def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
