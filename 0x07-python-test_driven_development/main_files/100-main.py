#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2]], [[3, 4], [100, 200]]))

m_a = [[1, 2, 3, 4], [4, 5, 6, 7]]
m_b = [[3, 4], [5, 6], [7, 8], [1, 2]]
print("result_1 is {}".format(matrix_mul(m_a, m_b)))

m_a = [[1.3, 2.7, 3.2, 4.5], [4, 5, 6, 7]]
m_b = [[3, 4], [5, 6.675], [7, 8.76], [1.0, 2.8]]
print("result_2 is {}".format(matrix_mul(m_a, m_b)))

m_a = [[13, 27, 33, 40], [49, 53, 67, 71], [10, 20, 54, 78]]
m_b = [[33, 44], [23, 54], [77, 86], [10, 28]]
print("result_3 is {}".format(matrix_mul(m_a, m_b)))
