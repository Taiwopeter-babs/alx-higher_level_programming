#!/usr/bin/python3
"""
    This module contains a class Rectangle that
    inherits from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation"""
        width = self.__width
        height = self.__height
        cls = type(self).__name__

        return "[{}] {}/{}".format(cls, width, height)
