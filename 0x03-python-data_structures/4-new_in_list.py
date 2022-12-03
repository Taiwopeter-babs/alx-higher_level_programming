#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    new_list = []

    if (idx < 0 or idx > length):
        new_list += my_list
        return (new_list)

    new_list += my_list
    new_list[idx] = element

    return (new_list)
