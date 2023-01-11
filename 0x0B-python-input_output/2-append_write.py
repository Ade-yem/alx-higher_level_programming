#!/usr/bin/python3

"""function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
        fliename (string): file to append to
        text (string): string to be added to file
    Returns:
        the number of characters appended to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
