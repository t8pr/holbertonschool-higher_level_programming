#!/usr/bin/python3
"""Module for print_matrix_integer function."""


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))
        if len(row) == 0:
            print()
