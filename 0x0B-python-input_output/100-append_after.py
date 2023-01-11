#!/usr/bin/python3
"""
    This module contains a function that appends
    a line of text to a file after a line containing a specific
    string
"""


def append_after(filename="", search_string="", new_string=""):
    """
        searches and appends a line of text

        Args:
            filename(str): name of file to be searched
            search_string(str): string to look out for
            new_string(str): line of text to be appended after
                search_string

        Assumptions are made that the file already exists
    """

    # read the whole file into a buffer
    with open(filename, mode="r", encoding="utf-8") as my_file:
        my_buffer = my_file.readlines()

    # open the file, truncating it and appending text
    with open(filename, mode="w", encoding="utf-8") as out_file:
        for line in my_buffer:
            if search_string in line:  # check if substring exists in line
                line += new_string
            out_file.write(line)
