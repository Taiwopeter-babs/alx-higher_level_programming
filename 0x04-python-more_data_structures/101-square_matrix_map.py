#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda matrix: list(map(lambda x: x**2, matrix)), matrix))
