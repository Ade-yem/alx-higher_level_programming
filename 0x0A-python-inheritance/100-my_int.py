#!/usr/bin/python3

"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        #return int.__ne__(self, value)
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        #return int.__eq__(self, value)
        return self.real == value
