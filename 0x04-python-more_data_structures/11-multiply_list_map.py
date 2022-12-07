#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    multiply_by2 = [] + list(map(lambda val: val * number, my_list))
    return (multiply_by2)
