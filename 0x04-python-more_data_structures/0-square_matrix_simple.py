#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if (not matrix):
        return

    new = [] + [list(map(lambda x: x ** 2, ma)) for ma in matrix]

    return (new)
