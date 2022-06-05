#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for elt in ligne:
            if ligne.index(elt) == len(ligne):
                print("{:d}".format(elt), end='')
            print("{:d}".format(elt), end=' ')
        print()
