#!/usr/bin/python3

"""Module for the base class of all the projects"""


class Base:
    """base class for all the projects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
