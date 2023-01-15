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
        return f"[Square] ({id}) {x}/{y} - {size}"

s1 = Square(5)
print(s1)
print(s1.area())
s1.display()

print("---")

s2 = Square(2, 2)
print(s2)
print(s2.area())
s2.display()

print("---")
            
s3 = Square(3, 1, 3)
print(s3)
print(s3.area())
s3.display()
                                                    
