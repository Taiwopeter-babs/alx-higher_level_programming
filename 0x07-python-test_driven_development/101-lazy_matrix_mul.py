#!/usr/bin/python3
"""
    This module contains a function takes in two matrices,
    and returns the result of their multiplicaion in a new matrix.
    `lazy` because unlike the module 100-matrix_mul.py, this uses
    Numpy to perform the calculation.

    Args:
        m_a: First arg. Must be list of list of integers.
        m_b: Second arg. Must be list of list of integers.

    Raises:
        TypeError: if any given argument doesn't conforn to the
            Args Requirements (see above)
        ValueError: if any of the argument is an empty list or list of lists.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the product of two matrices in a new matrix
    """
    err_msg_types_arg_0 = "only int/float types allowed in m_a"
    err_msg_types_arg_1 = "only int/float types allowed in m_b"

    err_row_size_a = "rows in m_a matrix cannot have varying lengths"
    err_row_size_b = "rows in m_b matrix cannot have varying lengths"

    # check for instance of arguments
    if not isinstance(m_a, list):
        raise TypeError("only list instance allowed in matrix_a")
    if not isinstance(m_b, list):
        raise TypeError("only list instance allowed in matrix_b")

    # validate that elements in arguments are lists
    for mat_a in m_a:
        if not isinstance(mat_a, list):
            raise TypeError("m_a can only be a list of lists")

    for mat_b in m_b:
        if not isinstance(mat_b, list):
            raise TypeError("m_b can only be a list of lists")

    # validate that each list is not empty
    if len(m_a) != 0:
        for mat_a in m_a:
            if len(mat_a) == 0:
                raise ValueError("empty list not allowed in argument m_a")
    else:
        raise ValueError("empty matrix not allowed in argument m_a")

    if len(m_b) != 0:
        for mat_b in m_b:
            if len(mat_b) == 0:
                raise ValueError("empty list not allowed in argument m_b")
    else:
        raise ValueError("empty matrix not allowed in argument m_b")

    # validate types - int and float - for each element in lists
    for mat_a in m_a:
        for ele in mat_a:
            if type(ele) not in [int, float]:
                raise TypeError(err_msg_types_arg_0)

    for mat_b in m_b:
        for ele in mat_b:
            if type(ele) not in [int, float]:
                raise TypeError(err_msg_types_arg_1)

    """
        check the lengths of lists in a matrix are equal
        if the lengths of each matrix is more than one
    """
    if len(m_a) > 1:
        for idx, mat in enumerate(m_a):
            if idx < len(m_a) - 1:
                if len(m_a[idx]) != len(m_a[idx + 1]):
                    raise TypeError(err_row_size_a)

    if len(m_b) > 1:
        for idx, mat in enumerate(m_b):
            if idx < len(m_b) - 1:
                if len(m_b[idx]) != len(m_b[idx + 1]):
                    raise TypeError(err_row_size_b)

    """
        length of column of first matrix must be equal to size of
        rows of second matrix.
    """
    for mat in m_a:
        len_a = len(mat)  # size of columns of first matrix
        break

    len_b = len(m_b)  # size of rows of second matrix

    if len_a != len_b:
        raise ValueError(
            "multiplication is not possible check the sizes of rows "
            "and columns of respective matrices"
        )

    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    resulting_matrix = np.matmul(matrix_a, matrix_b)

    return resulting_matrix
