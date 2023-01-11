#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (string): file to be read
    """
    with open(filename, "r", encoding="utf-8") as f:
        file = f.read()
        print(file, end="")
