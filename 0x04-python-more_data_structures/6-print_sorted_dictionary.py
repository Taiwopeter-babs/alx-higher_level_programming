#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if (not a_dictionary):
        return

    # sort the dictionary: returns a list of tuples [(key, value)]
    sorted_dict = sorted(a_dictionary.items())

    for key, value in sorted_dict:
        print("{}: {}".format(key, value))
