#!/usr/bin/python3
"""
    This module contains a function that returns
    a default dictionary object
"""


def class_to_json(obj):
    """
        Return a dictionary
    """

    return (getattr(obj, "__dict__"))
