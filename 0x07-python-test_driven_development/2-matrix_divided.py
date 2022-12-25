#!/usr/bin/python3
"""
    This module accepts a matrix and a divisor and,
    returns the result of division of each element in a list
    in the corresponding list index

    Args:
        matrix (list: int): This must be a list of list of integers or float
        div (int or float): second argument to function
"""


def matrix_divided(matrix, div):
    """
        Returns a list of list of floating point numbers
    """

    err_row_size = "Each row of the matrix must have the same size"
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    err_zero_division = "division by zero"

    if (not matrix):
        return (None)

    if (not isinstance(matrix, list)):
        raise TypeError(type_err)

    if (type(div) in [int, float]):
        if (div == 0):
            raise ZeroDivisionError(err_zero_division)
    else:
        raise TypeError("div must be a number")

    i = 0
    while (i < len(matrix) - 1):
        if (len(matrix[i]) != len(matrix[i + 1])):
            raise TypeError(err_row_size)
        i += 1

    for mat in matrix:
        if (not isinstance(mat, list)):
            raise TypeError(type_err)
        for ele in mat:
            if type(ele) not in [int, float]:
                raise TypeError(type_err)

    new = [[round(ele/div, 2) for ele in mat] for mat in matrix]
    return (new)
