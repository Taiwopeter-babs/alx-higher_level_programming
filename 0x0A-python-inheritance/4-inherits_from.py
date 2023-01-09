#!/usr/bin/python3
"""
    This module contains a function that checks
    instance of object
"""


def inherits_from(obj, a_class):
    """
    Returns boolean based on condition

    Args:
        obj: instance of python class
        a_class: class
    Return:
        True: if obj's class is a subclass of a_class
        False: if not or if type(obj) confirms
            equality with class
    """
    if type(obj) == a_class:
        return False

    return issubclass(type(obj), a_class)
