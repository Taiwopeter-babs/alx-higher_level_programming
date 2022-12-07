#!/usr/bin/python3


def weight_average(my_list=[]):
    if (not my_list):
        return (0)

    first_val = 0
    second_val = 0
    # unpack tuple with list comprehension
    mul_list = [] + [first * sec for (first, sec) in my_list]
    addn_list = [] + [sec for (first, sec) in my_list]

    # add the values of mul_list
    for val in mul_list:
        first_val += val
    # add values in addn_list
    for val2 in addn_list:
        second_val += val2

    weight_avg = first_val / second_val
    return (weight_avg)
