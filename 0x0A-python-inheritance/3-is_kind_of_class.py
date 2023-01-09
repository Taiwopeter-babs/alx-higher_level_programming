#!/usr/bin/python3
"""
    This module checks for instance and inheritance of first argument
    in function
"""


def is_kind_of_class(obj, a_class):
    """Returns boolean based on condition"""
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True

    return False
