#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    str_len = len(my_string)

    for char in my_string:
        if (char == "c" or char == "C"):
            continue
        new_string += char

    return (new_string)
