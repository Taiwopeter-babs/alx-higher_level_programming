#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = [[1, 2, 3, 4], [4, 5, 6, 7]]
m_b = [[3, 4], [5, 6], [7, 8], [1, 2]]
print(lazy_matrix_mul(m_a, m_b))


m_a = [[1.3, 2.7, 3.2, 4.5], [4, 5, 6, 7]]
m_b = [[3, 4], [5, 6.675], [7, 8.76], [1.0, 2.8]]
print(lazy_matrix_mul(m_a, m_b))


m_a = [[13, 27, 33, 40], [49, 53, 67, 71], [10, 20, 54, 78]]
m_b = [[33, 44], [23, 54], [77, 86], [10, 28]]
print(lazy_matrix_mul(m_a, m_b))
