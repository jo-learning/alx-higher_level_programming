#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    elif matrix != [[]]:
        for i in range(len(matrix)):
            j = 0
            while(j < len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                j = j + 1
            print()
