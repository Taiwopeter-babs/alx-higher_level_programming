#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(my_list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(my_list) == 0:
        return None

    if (not isinstance(my_list, list)):
        raise TypeError

    idx = 0
    while (idx < len(my_list)):
        if (not isinstance(my_list[idx], int)):
            raise TypeError("element not an integer")
        idx += 1

    result = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > result:
            result = my_list[i]
        i += 1
    return result
