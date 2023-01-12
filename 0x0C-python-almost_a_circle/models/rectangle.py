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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        row = self.__height
        col = self.__width
        x = self.__x  # x-co-ordinate
        y = self.__y  # y-co-ordinate

        print("\n" * y, end='')
        for i in range(row):
            print(" " * x, end='')
            for j in range(col):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a string representation of class"""
        x = self.__x
        y = self.__y
        _id = self.id
        w = self.__width
        h = self.__height

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                _id, x, y, w, h)

    def update(self, *args, **kwargs):
        """Update attributes with variable orderly arguments"""
        
        if (args is not None and len(args) > 0):
            args_value = [arg for arg in args]

            try:
                self.id = args_value[0]
                self.__width = args_value[1]
                self.__height = args_value[2]
                self.__x = args_value[3]
                self.__width = args_value[4]
            except:
                pass
        else:
            if kwargs is not None:
                for key, val in kwargs.items():
                    if key == 'width':
                        self.__width = kwargs[key]
                    elif key == 'height':
                        self.__height = kwargs[key]
                    elif key == 'x':
                        self.__x = kwargs[key]
                    elif key == 'y':
                        self.__y = kwargs[key]
                    elif key == 'id':
                        self.id = kwargs[key]
