#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if (matrix == []):
        print()

    for row in matrix:
        for value in row:
            print("{:d}".format(value), end=' ')
        print()
