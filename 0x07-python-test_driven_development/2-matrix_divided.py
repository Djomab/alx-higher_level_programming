#!/usr/bin/python3
"""Matrix module"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides all elements of a matrix

    Args:
        matrix: a list of lists of integers or floats
        div: a number (integer or float)
    """
    new_list = []
    if not any(isinstance(ligne, list) for ligne in matrix):
        raise TypeError("matrix must be a matrix" +
                        "(list of lists) of integers/floats")
    elif not all(len(matrix[0]) == len(ligne) for ligne in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for ligne in matrix:
        for element in enumerate(ligne):
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix" +
                                "(list of lists) of integers/floats")
            else:
                new_list = list(map(lambda y: list(
                    map(lambda x: round(x / div, 2), y)), matrix))
    return new_list
