#!/usr/bin/python3


def uniq_add(my_list=[]):
    if (not my_list):
        return

    # convert to set to remove duplicate items and back to list
    new = list((set(my_list)))

    sum = 0
    for num in new:
        sum += num

    return (sum)
