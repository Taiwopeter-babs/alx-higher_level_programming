#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    matrix_rev = '\n'.join([' '.join(["{:d}".format(val) for val in row])
                            for row in matrix])
    print(matrix_rev)
