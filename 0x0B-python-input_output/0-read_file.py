#!/usr/bin/python3


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
