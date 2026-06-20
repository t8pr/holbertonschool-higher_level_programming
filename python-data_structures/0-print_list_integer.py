#!/usr/bin/python3
"""Module for print_list_integer function."""


def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
