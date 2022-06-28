#!/usr/bin/python3


def print_square(size):
    """
    print square with #

    args:
        size: size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * "#")