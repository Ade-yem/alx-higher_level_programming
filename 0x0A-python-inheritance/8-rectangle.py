#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
a class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Instantiation with width and height
        Args:
            height (int): private attribute
            width (int): private attribute
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
