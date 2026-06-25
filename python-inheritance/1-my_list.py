#!/usr/bin/python3
"""
This module provides a custom list class that adds a print_sorted method.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying 
        the original list.
        """
        print(sorted(self))
