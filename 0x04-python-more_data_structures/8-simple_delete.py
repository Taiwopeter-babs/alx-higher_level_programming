#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if (not a_dictionary):
        return

    if (key not in a_dictionary):
        return (a_dictionary)

    del a_dictionary[key]

    return (a_dictionary)
