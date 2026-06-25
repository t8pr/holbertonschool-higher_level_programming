#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """Class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverted equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality operator"""
        return super().__eq__(other)
