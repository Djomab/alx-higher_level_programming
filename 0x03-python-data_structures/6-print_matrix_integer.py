#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for elt in ligne:
            print("{:d}".format(elt), end='')
            if elt != ligne[-1]:
                print(end=' ')
        print()
