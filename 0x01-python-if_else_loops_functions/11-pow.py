#!/usr/bin/python3

def pow(a, b):
    result = 1
    if b >= 0:
        for  i in range(b, 0, -1):
            result = result * a
    else:
        for i in range(0, (-1 * b)):
            result = result * (1 / a)
    return result
