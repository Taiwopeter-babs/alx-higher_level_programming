#!/usr/bin/python3
"""
    This module contains a class Square that
    inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This class inherits Rectangle class"""

    def __init__(self, size):
        self.__size = size

        super().__init__(self.__size, self.__size)
        super().integer_validator("size", self.__size)
        super().__str__()

    def area(self):
        """Returns the area"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation"""
        size = self.__size
        cls = type(self).__name__

        return "[{}] {}/{}".format(cls, size, size)
