#!/usr/bin/python3
"""
    This module contains a function that returns a list
"""


def lookup(obj):
    """
    Returns available attributes and methods of an object
    in a list

    Args:
        obj: a class or instance of class
    """
    return dir(obj)
