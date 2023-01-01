#!/usr/bin/python3
"""

a function that divides all elements of a matrix.

"""

def matrix_divided(matrix, div):
    """
     divides all elements of a matrix

    Args:
        matrix (list): A list of integers or floats
        div (int): the divisor

    Returns: a new matrix
    """
    lent = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if  not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if lent != 0 and len(i) != lent:
                    raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        lent = len(i)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
