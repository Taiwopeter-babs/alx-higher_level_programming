#!/usr/bin/python3
"""
    This module contains a function takes in two matrices,
    and returns the result of their multiplicaion in a new matrix.

    Args:
        m_a: First arg. Must be list of list of integers.
        m_b: Second arg. Must be list of list of integers.

    Raises:
        TypeError: if any given argument doesn't conforn to the
            Args Requirements (see above)
        ValueError: if any of the argument is an empty list or list of lists.
"""


def matrix_mul(m_a, m_b):
    err_msg_types_arg_0 = "m_a should contain only integers or floats"
    err_msg_types_arg_1 = "m_b should contain only integers or floats"

    err_row_size_a = "each row of m_a must be of the same size"
    err_row_size_b = "each row of m_b must be of the same size"

    # check for instance of arguments
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # validate that elements in arguments are lists
    for mat_a in m_a:
        if not isinstance(mat_a, list):
            raise TypeError("m_a must be a list of lists")

    for mat_b in m_b:
        if not isinstance(mat_b, list):
            raise TypeError("m_b must be a list of lists")

    # validate that each list is not empty
    if len(m_a) != 0:
        for mat_a in m_a:
            if len(mat_a) == 0:
                raise ValueError("m_a can't be empty")
    else:
        raise ValueError("m_a can't be empty")

    if len(m_b) != 0:
        for mat_b in m_b:
            if len(mat_b) == 0:
                raise ValueError("m_b can't be empty")
    else:
        raise ValueError("m_b can't be empty")

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
        raise ValueError("m_a and m_b can't be multiplied")

    resulting_matrix = [
        [sum(a * b for a, b in zip(mat_a, mat_b)) for mat_b in zip(*m_b)]
        for mat_a in m_a
    ]
    return resulting_matrix
