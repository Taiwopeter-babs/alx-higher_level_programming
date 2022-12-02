#!/usr/bin/python3


def print_list_integer(my_list=[]):

    length = len(my_list)

    idx = 0
    while (idx < length):
        print("{:d}".format(my_list[idx]))

        idx += 1
