#!/usr/bin/python3

"""
a function that returns True if the object is exactly
 an instance of the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is exactly an
    instance of the specified class, otherwise False
    Return:
        True if the object is exactly an instance of the
        specified class ; otherwise False
    """
    return True if isinstance(obj, a_class) else False
