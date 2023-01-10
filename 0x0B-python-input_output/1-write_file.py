#!/usr/bin/python3
"""
    This module contains a function that performs i/o
"""


def write_file(filename="", text=""):
    """
    Writes to a file

    Args:
        filename(str): filename of file to be read
        text: bytes to be written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        chars_written = my_file.write(text)

    return chars_written
