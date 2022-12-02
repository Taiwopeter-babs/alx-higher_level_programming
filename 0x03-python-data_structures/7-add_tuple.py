#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if (len1 >= 2 and len2 >= 2):
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        new_tuple = (a, b)

    elif (len1 >= 2 and len2 < 2):
        if (len2 == 1):
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + 0
            new_tuple = (a, b)
        elif (len2 == 0):
            a = tuple_a[0] + 0
            b = tuple_a[1] + 0
            new_tuple = (a, b)

    elif (len1 < 2 and len2 >= 2):
        if (len1 == 1):
            a = tuple_a[0] + tuple_b[0]
            b = 0 + tuple_b[1]
            new_tuple = (a, b)
        elif (len1 == 0):
            a = 0 + tuple_b[0]
            b = 0 + tuple_b[1]
            new_tuple = (a, b)

    elif (len1 < 2 and len2 < 2):
        a = tuple_a[0] + tuple_b[0]
        b = 0
        new_tuple = (a, b)

    return (new_tuple)
