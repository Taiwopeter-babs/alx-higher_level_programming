#!/usr/bin.python3
"""
    This module contains a function that prints a square

    Args:
        size (int): size of square

    Raises:
        ValueError: if size is less than 0
        TypeError: if type or instance of size is not an integer
    Example:
        >>> print_square(3)
        ###
        ###
        ###
"""


def print_square(size):
    """Prints square with '#' character"""

    type_err = "size must be an integer"
    value_err = "size must be >= 0"

    if (not isinstance(size, int)):
        raise TypeError(type_err)

    if (size < 0):
        raise ValueError(value_err)

    if (isinstance(size, float) and size < 0):
        raise TypeError(type_err)

    i = 0
    while (i < size):

        j = 0
        while (j < size):
            print("#", end='')
            j += 1

        print()
        i += 1
