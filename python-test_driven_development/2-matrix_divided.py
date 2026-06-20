#!/usr/bin/python3
"""Module for dividing all elements of a matrix.

This module provides a function to divide every element
of a matrix by a given divisor, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Returns a new matrix with elements rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    row_size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
