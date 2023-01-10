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

    def to_json(self):
        """
            Returns a dictionary
        """

        return (getattr(self, "__dict__"))
