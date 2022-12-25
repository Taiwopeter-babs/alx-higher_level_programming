#!/usr/bin/python3

"""
    This module takes in two string arguments and prints formatted
    output.

    Args:
        first_name (str): first parameter
        last_name (str): second parameter
    Raises:
        TypeError: if either of the arguments is not a string
"""


def say_my_name(first_name, last_name=""):
    """Prints formatted output of argument"""

    first_name_err = "first_name must be a string"
    last_name_err = "last_name must be a string"

    if (not isinstance(first_name, str)):
        raise TypeError(first_name_err)

    elif (not isinstance(last_name, str)):
        raise TypeError(last_name_err)

    else:
        print("My name is {} {}".format(first_name, last_name))
