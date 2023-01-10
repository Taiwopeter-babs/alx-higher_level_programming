#!/usr/bin/python3
"""
    This module contains a function that performs i/o
"""


def read_file(filename=""):
    """
    Reads from a file

    Args:
        filename(str): filename of file to be read
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')
