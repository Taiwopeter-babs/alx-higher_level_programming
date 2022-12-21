#!/usr/bin/python3
"""This module calculates the area and circumference"""
import math
import dis


class MagicClass:
    """Instantiates radius attribute after validation and returns methods"""

    def __init__(self, radius):
        """This instantiates the radius attribute
        Args:
            radius (int or float): attribute to be validated
        """

        if (type(radius) is not int or type(float) is not float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

        def area(self):
            """Returns area"""
            return ((self.__radius ** 2) * math.pi)

        def circumference(self):
            """Returns circumference"""
            return (2 * math.pi * self.__radius)
print(dis.dis(MagicClass))
