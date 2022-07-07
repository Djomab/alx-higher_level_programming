#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """Return list of lists of n integers in pascal's triangle"""
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        ligne = [1]
        for j in range(len(pascal)):
            if j+1 < len(pascal):
                ligne.append(pascal[i-1][j] + pascal[i-1][j+1])
        ligne.append(1)
        pascal.append(ligne)

    return pascal
