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
        super(Square, self.__class__).height.fset(self, size)
        super(Square, self.__class__).x.fset(self, x)
        super(Square, self.__class__).y.fset(self, y)

    @property
    def size(self):
        """Setter and getter methods for size"""
        return self.width

    @size.setter
    def size(self, size):
        super(Square, self.__class__).width.fset(self, size)
        self.width = size  # width
        self.height = size  # height

    def __str__(self):
        """Returns a string representation of class"""
        _x = self.x
        _y = self.y
        _id = self.id
        _size = self.width

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             _id, _x, _y, _size)

    def update(self, *args, **kwargs):
        """Update attributes"""
        if (len(args) > 0):
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
            return

        if kwargs is not None:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of class"""
        return {"id": getattr(self, "id"),
                "size": getattr(self, "size"),
                "x": getattr(self, "x"),
                "y": getattr(self, "y")}
