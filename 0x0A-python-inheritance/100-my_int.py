#!/usr/bin/python3
"""
    This module contains a class MyInt that inherits
    from int class
"""

class MyInt(int):
    """
        MyInt class inherits from int class
    """
    def __eq__(self, other):
        """Inverts the equality method"""
        if (isinstance(other, self.__class__)):
            return self != other
        return False

    def __ne__(self, other):
        """Inverts the not-equal method"""
        return not self.__eq__(other)

    def __str__(self):
        return "%d" % int(self)
