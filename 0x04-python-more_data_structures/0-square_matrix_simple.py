#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(lambda submatrix: list(lambda i: i**2, submatrix), matrix )
