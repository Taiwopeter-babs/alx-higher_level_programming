#!/usr/bin/python3
"""
    This module contains a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
       Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
           class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Setter and getter methods for width"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Setter and getter methods for height"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Setter and getter methods for x"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Setter and getter methods for y"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Computes area of Rectangle"""
        w = self.__width
        h = self.__height
        area = w * h

        return (area)

    def display(self):
        """prints the shape of rectangle with "#" """
        row = self.height
        col = self.width
        x = self.x  # x-co-ordinate
        y = self.y  # y-co-ordinate

        print("\n" * y, end='')
        for i in range(row):
            print(" " * x, end='')
            for j in range(col):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a string representation of class"""
        x = self.x
        y = self.y
        _id = self.id
        w = self.width
        h = self.height

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                _id, x, y, w, h)

    def update(self, *args, **kwargs):
        """Update attributes with variable orderly arguments"""

        if (args is not None and len(args) > 0):

            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
            return
        if kwargs is not None:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """Returns a dictionary representation of class"""
        return {"id": getattr(self, "id"),
                "width": getattr(self, "width"),
                "height": getattr(self, "height"),
                "x": getattr(self, "x"),
                "y": getattr(self, "y")}
