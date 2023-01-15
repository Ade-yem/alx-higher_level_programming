#!/usr/bin/python3

"""Module for the class Rectangle that defines a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): position x
            y (int): position y
            id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets/sets the value of height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets/sets the value of position y of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ defines the area value of the Rectangle instance.
        Return:
           the area value of the Rectangle instance.
        """
        return self.height * self.width

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        by taking care of x and y"""
        if self.y > 0:
            for k in range(self.y):
                print()

        for i in range(0, self.height):
            for a in range(self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ overriding the __str__ method
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        x = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        y = f"- {self.width}/{self.height}"
        return x + y

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        attrs = ["id", "width", "height", "x", "y"]
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
