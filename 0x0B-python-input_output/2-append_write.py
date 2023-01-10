#!/usr/bin/python3
"""
    This module contains a function that performs i/o
"""


def append_write(filename="", text=""):
    """
    Appends to a file

    Args:
        filename(str): filename of file to be written to
        text: bytes of characters to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        chars_appended = my_file.write(text)

    return (chars_appended)
