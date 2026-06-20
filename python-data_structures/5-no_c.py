#!/usr/bin/python3
"""Module for no_c function."""


def no_c(my_string):
    """Removes all characters c and C from a string."""
    return "".join([ch for ch in my_string if ch != 'c' and ch != 'C'])
