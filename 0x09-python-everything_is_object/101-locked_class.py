#!/usr/bin/python3
"""
    This module contains a class `LockedClass` that limits
    the dynamic creation of attributes at runtime
"""


class LockedClass:
    """
        Empty class that limits the dynamic creation of
        attribute to `first_name`
    """
    __slots__ = "first_name"
