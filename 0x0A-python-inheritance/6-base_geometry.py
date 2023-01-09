#!/usr/bin/python3
"""
    This module contains a class
    with an exception method
"""


class BaseGeometry:
    """This class contains a method that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
