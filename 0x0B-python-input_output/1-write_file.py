#!/usr/bin/python3

"""Module defines a function that writes to a text file.."""


def write_file(filename="", text=""):
    """Write a string to a text file in UTF8 Format.
    Args:
        filename (str): Name of File to write to
        text (str): text to write to file
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
