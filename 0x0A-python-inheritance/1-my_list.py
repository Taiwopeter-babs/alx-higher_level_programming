#!/usr/bin/python3
"""
    This module contains a class that inherits from list class
"""


class MyList(list):
    """
    class inherits from list class and sorts the list
    without altering the original list
    """

    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
