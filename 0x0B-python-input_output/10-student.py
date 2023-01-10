#!/usr/bin/python3
"""
    This module contains a class Student
"""


class Student:
    """class contains instantiation method and to_json method"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary
        """

        # check if attrs is a list and not empty
        if type(attrs) is list and len(attrs) > 0:
            new = {}
            for item in attrs:
                if type(item) is not str:
                    return getattr(self, "__dict__")
                if not hasattr(self, item):  # check for existence of attribute
                    continue
                new[item] = getattr(self, item)

            return new

        return getattr(self, "__dict__")
