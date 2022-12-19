#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function, safely.


    Params:
            fct: pointer to function to be executed
            args: variable number of arguments to fct
    Return: result of the function, otherwise None and print
            to stderr the Exception
    """
    try:
        if not fct(*args):
            raise Exception
    except (TypeError, ValueError, Exception) as err:
        print("Exception:", err, file=sys.stderr)
        return (None)
    else:
        return (fct(*args))
