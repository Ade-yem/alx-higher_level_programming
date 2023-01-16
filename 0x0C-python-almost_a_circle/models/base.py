#!/usr/bin/python3

"""Module for the base class of all the projects"""
import json
import os.path
import csv
import turtle


class Base:
    """base class for all the projects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if type(list_dictionaries) == list:
            if list_dictionaries is None or len(list_dictionaries) == 0:
                return "[]"
            else:
                return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): is a list of instances who inherits of Base
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                lists = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of the JSON string representation json_string
        Args:
            json_string is a string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): double pointer to a dictionary
        """
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                r1 = cls(1, 2)
            else:
                r1 = cls(2)
            r1.update(**dictionary)
            return r1

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            lists = f.read()
            list_dict = cls.from_json_string(lists)
            return [cls.create(**d) for d in list_dict]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                writer = csv.writer(f)
                writer.writerows([])
            else:
                if cls.__name__ == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                else:
                    attrs = ["id", "size", "x", "y"]
                lists = [i.to_dictionary() for i in list_objs]
                writer = csv.DictWriter(f, fieldnames=attrs)
                for i in lists:
                    writer.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
           Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"
        if os.path.exists(filename) is False:
            return []
        with open(filename, newline='') as f:
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            else:
                attrs = ["id", "size", "x", "y"]
            reader = csv.DictReader(f, fieldnames=attrs)
            list_dict = [dict([k, int(v)] for k, v in row.items())
                         for row in reader]
            return [cls.create(**d) for d in list_dict]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
