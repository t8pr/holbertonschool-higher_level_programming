#!/usr/bin/python3
"""Module for square_matrix_simple function."""


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
