#!/usr/bin/python3
"""
    This module contains a function that
    prints the computed metrics based on input
    in stdin

    Explanation: The possible status codes are put in a dictionary
                 and set to 0. The function reads a line from stdin
                 and splits it, returning a list object.

                 The try...except block is to ensure status code is
                 available, otherwise moves to next line
"""
import sys


def print_status_and_value():
    """
        prints status codes and values
    """
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    count = 0

    for line in sys.stdin:
        # split the line to give a list object
        this_line = line.split()
        try:
            """
                Get status code from line, increment the value
                in the status_code dictionary, and store file size of line
                summing it in subsequent lines
            """
            code = this_line[-2]
            status_codes[code] += 1
            file_size += int(this_line[-1])

        except None:  # if status code is None
            continue

        """
            Count begins from 0, 9 is the 10th value;
            reset count if count == 9 after operation and increment by 1
            so the next condition begins printing.
            Check if value of key has been incremented from
            line 39; if so, print code and value
            Same condition applies if count < 9
        """
        if (count == 9):
            print("File size: {}".format(file_size))

            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            count = 0
        count += 1

        if (count < 9):
            print("File size: {}".format(file_size))

            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status_and_value()
