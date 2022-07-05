#!/usr/bin/python3



def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8)
    Args:
        filename: name of file to write to
        text: text to write to the file
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

