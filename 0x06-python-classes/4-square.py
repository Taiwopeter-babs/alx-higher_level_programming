#!/usr/bin/python3
"""
    This module contains a class Square with a private attribute
    A check is put to ensure that the type of value and its magnitude
    are integers and >= 0 respectively

    The getter and setter are set appropriately.
"""


class Square:
    """This class is initialized with an attribute. Defines a square size
    """

    def __init__(self, size=0):
        """Initialization of attribute size.
            A check is done to ascertain that the data type of size is an
            integer, and it is equal to zero or a positive integer

        Args:
            size: An attribute of the class that defines the size of a square
                its visibility and type validation are managed in the setter
        """

        self.size = size

    @property
    def size(self):
        """Returns the size after validation and after
        it has been set to the attribute

        Args:
            size (int): private attribute that must be an integer and >= 0

        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer

        Returns:
            private attribute of object/instance

        """
        return (self.__size)

    @size.setter
    def size(self, size):
        try:
            if (type(size) != int):
                raise TypeError("size must be an integer")
            if (size < 0):
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError):
            raise

        else:
            self.__size = size

    def area(self):
        """Returns the area of the square size

        Returns:
            integer value of area

        """
        return (self.__size ** 2)
