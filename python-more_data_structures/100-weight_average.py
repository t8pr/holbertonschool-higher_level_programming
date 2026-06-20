#!/usr/bin/python3
"""Module for weight_average function."""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if not my_list:
        return 0
    total = sum(score * weight for score, weight in my_list)
    weights = sum(weight for score, weight in my_list)
    return total / weights
