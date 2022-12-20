#!/usr/bin/python3
"""
    This module contains a class Square with a private attribute
    A check is put to ensure that the type of value and its magnitude
    are integers and >= 0 respectively
"""


class Square:
    """This class is initialized with an attribute. Defines a square size

    """

    def __init__(self, size=0):
        """Initialization of attribute size.
            A check is done to ascertain that the data type of size is an
            integer.

        Args:
            size: A private attribute that defines the size of a square

        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer

        """
        try:
            if (type(size) != int):
                raise TypeError("size must be an integer")
            if (size < 0):
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError):
            raise
        else:
            self.__size = size
