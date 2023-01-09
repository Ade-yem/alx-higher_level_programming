#!/usr/bin/python3

"""
class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    Args:
        list: list of the class
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        lis = self.copy()
        lis.sort()
        print(lis)
