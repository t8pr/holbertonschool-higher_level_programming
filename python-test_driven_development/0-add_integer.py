#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function to add two integers or floats,
casting floats to integers before performing the addition.
"""


def add_integer(a, b=98):
    """Adds two integers or floats after casting to int.

    Returns the integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
