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

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""
        obj = vars(self)
        if type(attrs) is list:
            for ele in attrs:
                if type(ele) != str:
                    return obj
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
