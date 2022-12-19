#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer value


    Params:
            value: argument to be printed
    Return:
            Boolean:
                    True if value is an integer and correctly printed
                    otherwise False
    """
    try:
        print("{:d}".format(value))

    except (TypeError, ValueError):
        return (False)

    return (True)
