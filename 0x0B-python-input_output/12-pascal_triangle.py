#!/usr/bin/python3
"""
    This module contains a function that
    returns a list of lists of patterns
    of the pascal's triangle
"""


def pascal_triangle(n):
    """
        Returns a list of lists of
        a pattern of pascal's triangle
    """
    in_arr = []
    outer_arr = []

    if (n <= 0):
        return []

    row = 0
    while (row < n):

        col = 0
        while (col <= row):

            if row == 0 or col == 0:
                pasc_coef = 1
            else:
                pasc_coef *= (row - col + 1) / col

            in_arr.append(int(pasc_coef))
            col += 1
        outer_arr.append(in_arr)
        in_arr = []
        row += 1

    return outer_arr
