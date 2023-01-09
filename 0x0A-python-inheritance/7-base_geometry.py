#!/usr/bin/python3

"""
 class BaseGeometry.
"""


class BaseGeometry:
    """an empty class BaseGeometry."""
    def area(self):
        """ raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value
        Args:
            name: a string
            value: an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
