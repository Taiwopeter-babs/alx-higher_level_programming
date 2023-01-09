#!/usr/bin/python3
"""
    This module checks for instance of first argument
    in function
"""


def is_same_class(obj, a_class):
    """Returns boolean based on condition"""
    if type(obj) is a_class:
        return True

    return False
