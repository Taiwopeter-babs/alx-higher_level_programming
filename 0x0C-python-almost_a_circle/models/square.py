#!/usr/bin/python3
"""
    This module contains a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       Square class inherits Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
           class constructor
        """
        super().__init__(size, size, x, y, id)
        super(Square, self.__class__).width.fset(self, size)
        super(Square, self.__class__).height.fset(self, size)
        super(Square, self.__class__).x.fset(self, x)
        super(Square, self.__class__).y.fset(self, y)
    
    @property
    def size(self):
        """Setter and getter methods for size"""
        return self.width
    
    @size.setter
    def size(self, size):      
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size  # width
        self.height = size  # height

    def __str__(self):
        """Returns a string representation of class"""
        x = self.x
        y = self.y
        _id = self.id
        size = self.width

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                                _id, x, y, size)
