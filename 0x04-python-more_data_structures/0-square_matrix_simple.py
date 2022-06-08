#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[element**2 for element in ligne] for ligne in matrix]
