#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for mat in matrix:
        if len(mat) == 0:
            print()
        else:
            for i in range(len(mat)):
                print("{:d}".format(mat[i]), end="\n" if i == len(mat)-1 else " ")
