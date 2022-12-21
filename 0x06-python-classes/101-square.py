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

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of attribute size.
            A check is done to ascertain that the data type of size is an
            integer, and it is equal to zero or a positive integer

        Args:
            size (int): An attribute of the class that defines
                the size of a square. Its visibility and type validation
                are managed in the setter
            position (tuple: int): The elements at different
                indexes must be integers
        """
        self.__position = position
        self.__size = size

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
    def size(self, value):
        try:
            if (not isinstance(value, int)):
                raise TypeError("size must be an integer")
            if (size < 0):
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError):
            raise

        else:
            self.__size = value

    @property
    def position(self):
        """Getter method of position
            This returns the position after validation by the setter

        Args:
            value (int): To be validated by the setter

        Raises:
            TypeError: if position is not a tuple of two positive integers

        Returns:
            position -> tuple
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        try:
            for idx, item in enumerate(value):
                if (value[idx] < 0 or not isinstance(value[idx], int) or
                        len(value) != 2):
                    raise TypeError("position must be a tuple"
                                    "of 2 positive integers")
            if (not isinstance(value, tuple)):
                raise TypeError("position must be a tuple"
                                "of 2 positive integers")
        except TypeError:
            raise
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square size

        Returns:
            integer value of area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Returns a square shape with '#' characters.
            Its size depends on value entered in object.
        """
        size = self.__size
        pos = self.__position

        if (self.__size == 0):
            return ('\n')

        return '\n'.join(' ' * pos[0] + '#' * size for row in range(size))

    def __str__(self):
        """Returns a string representation of object"""

        return ("{}".format(self.my_print()))
