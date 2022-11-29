#!/usr/bin/python3


def print_last_digit(number):
    num = number
    if (num < 0):
        num *= -1
        res = num % 10
    res = num % 10
    print(res, end='')
    return (res)
