#!/usr/bin/python3
"""
    This module contains a class Rectangle
"""


class Rectangle:
    """
    This is a class with initialized fields, and
    encapsulated data.
    """

    def __init__(self, width=0, height=0):
        """
        Intialization of optional fields

        Args:
            width (int): if not given, default is 0
            height (int): if not given, default is 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Sets and returns the width of rectangle

        Args:
            value (int): must be an integer and >= 0

        Returns:
            An integer value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Sets and returns the height of rectangle

        Args:
            value (int): must be an integer and >= 0
        Returns:
            An integer value
        Raises:
            TypeError: if value is not an integer
            ValuError: if value is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value
