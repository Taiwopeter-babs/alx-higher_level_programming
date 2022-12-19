#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer value


    Params:
            value: argument to be printed
    Return:
            Boolean:
                    True if value is an integer and correctly printed
                    otherwise False and prints Exception error to stderr
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError, Exception) as err:
        print("Exception:", err, file=sys.stderr)
        return (False)

    return (True)
