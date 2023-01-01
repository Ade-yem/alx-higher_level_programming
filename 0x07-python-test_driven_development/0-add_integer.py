#!/usr/bin/python3

"""

 A function that adds 2 integers.

"""

def add_integer(a, b=98):
    """  adds 2 integers

    Args:
        a (int or float) : first parameter
        b (int or float) : second parameter
    
    Returns:
        n integer which is the addition of a and b

    Raises:
        TypeError if a or b is not int/float

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
        
