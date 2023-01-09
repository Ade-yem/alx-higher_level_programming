#!/usr/bin/python3

"""
 a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size size must be private. No getter or setter"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
