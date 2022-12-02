#!/usr/bin/python3


def max_integer(my_list=[]):

    if (not my_list):
        return (None)

    else:
        list_len = len(my_list)

        val = my_list[0]
        idx = 0
        while (idx < list_len):
            temp = my_list[idx]

            if (temp > val):
                val = temp
            idx += 1
    return (val)
