#!/usr/bin/python3

"""Contains function that ppends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
        filename: name of filename to be readen
        text: text str to appended to file
    Return:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
