#!/usr/bin/python3

"""Module for the square class that inherits from the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines square that inherits the rectangles properties and methods"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor
        Args:
            size (int): size of the square
            x (int): position x
            y (int): position y
            id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method of the rectangle"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """get/set size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attrs[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, "width", v)
                    setattr(self, "height", v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
