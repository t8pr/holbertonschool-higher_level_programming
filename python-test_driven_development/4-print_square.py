#!/usr/bin/python3
"""Module for printing a square.

This module provides a function that prints a square
of a given size using the '#' character.
"""


def print_square(size):
    """Prints a square with the character '#'.

    Raises TypeError if size is not an integer, ValueError if size < 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
