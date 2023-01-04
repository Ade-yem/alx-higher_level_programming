#!/usr/bin/python3

""" Class Rectangle that defines a rectangle"""


class Rectangle:
    """ Rectangle that defines a rectangle

    Attributes:
        width (int): Width of the rectangle
        height (int): height of the rectangle
    """
    number_of_instances = 0
    """int: number of instances created"""

    def __init__(self, width=0, height=0):
        """ Instantiation with optional default width and height
        Args:
            width (int): Width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        """ gets/sets the value of height of the rectangle """
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

    def __str__(self):
        """Define the print() and str representation of the rectangle."""
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(0, self.__height):
            rec += ("#" * self.__width) + "\n"
        return rec[:-1]

    def __repr__(self):
        """Define the repr representation of the rectangle"""
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        """Detect instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
