#!/usr/bin/python3


def number_keys(a_dictionary):
    if (not a_dictionary):
        return

    new = list(a_dictionary)

    total = 0
    for key in new:
        total += 1

    return (total)
