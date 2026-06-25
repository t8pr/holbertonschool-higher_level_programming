#!/usr/bin/python3
"""
This module contains a function that looks up attributes of an object.
"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)

