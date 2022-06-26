#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided
""" print("======== Normal usage ============")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix) """

""" print("======== Not same size ============")
matrix = [
    [1, 2, 3],
    [4, 5, 6, 1]
]
print(matrix_divided(matrix, 3))
print(matrix) """

print("======== Case element are not int, float ============")
matrix = [
    [1, 2, 3],
    ['4', 5, 'string',]
]
print(matrix_divided(matrix, 3))
print(matrix)
