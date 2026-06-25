#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
