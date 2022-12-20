#!/usr/bin/python3
"""
    This module contains a class Square with a private attribute
"""


class Square:
    """This class is initialized with an attribute. Defines a square size

    """

    def __init__(self, size):
        """Initialization of attribute size

        Args:
            size: A private attribute that defines the size of a square

        """
        self.__size = size
