#!/usr/bin/python3

"""class Student that defines a student"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of the class
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return vars(self)
