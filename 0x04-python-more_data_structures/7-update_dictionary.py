#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if (not a_dictionary):
        if (not key):
            return
        else:
            a_dictionary[key] = value

    if (key in a_dictionary):
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return (a_dictionary)
