#!/usr/bin/python3
"""
    This module contains a class Rectangle
"""


class Rectangle:
    """
    This is a class with initialized fields, and
    encapsulated data.

    Attributes:
        number_of_instances (int): public class attribute
        print_symbol (any): variable of any type to be printed
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Intialization of optional fields

        Args:
            width (int): if not given, default is 0
            height (int): if not given, default is 0
        """
        self.__width = width
        self.__height = height

        type(self).number_of_instances += 1

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
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
        except (TypeError, ValueError):
            raise

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
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        except (TypeError, ValueError):
            raise

        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        w = self.__width
        h = self.__height
        area = w * h

        return area

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            perimeter = 0
            return perimeter

        perimeter = 2 * (w + h)
        return perimeter

    def __str__(self):
        """Returns a string representation of pattern"""

        width = self.__width
        height = self.__height
        symbol = str(self.print_symbol)

        if width == 0 or height == 0:
            return ""

        return "\n".join(symbol * width for row in range(height))

    def __repr__(self):
        """Returns a formal string representation"""

        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Destructor of class Rectangle instance"""

        type(self).number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the instance of Rectangle with the larger area"""

        err_msg_1 = "rect_1 must be an instance of Rectangle"
        err_msg_2 = "rect_2 must be an instance of Rectangle"

        if not isinstance(rect_1, Rectangle):
            raise TypeError(err_msg_1)
        if not isinstance(rect_2, Rectangle):
            raise TypeError(err_msg_2)

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
