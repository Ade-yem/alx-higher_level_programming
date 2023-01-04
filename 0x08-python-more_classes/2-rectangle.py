#!/usr/bin/python3

""" Class Rectangle that defines a rectangle"""

class Rectangle:
    """ Rectangle that defines a rectangle

    Attributes:
        width (int): Width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional default width and height
        Args:
            width (int): Width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ gets/sets the value of width of the rectangle """
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets\sets the value of height of the rectangle """
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ Perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

