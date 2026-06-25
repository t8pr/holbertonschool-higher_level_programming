#!/usr/bin/python3
"""Module for safe_print_integer_err function."""
import sys


def safe_print_integer_err(value):
    """Prints an integer, prints error to stderr if not integer."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
