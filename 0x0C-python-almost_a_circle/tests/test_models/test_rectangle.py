#!/usr/bin/python3

"""Unittest module for the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch
import sys


class TestRectangleMethods(unittest.TestCase):
    """Unittest suite for the Rectangle class methods"""

    def test_default_id(self):
        """tests the default id of the object"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_with_id(self):
        """tests the rectangle with id arg passed"""
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    """Validation"""

    def test_attribute_type(self):
        """test all attribute types with all data types except integers"""
        r4 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, "two", 0, 0, 12)
        with self.assertRaises(TypeError):
            r4.x = {}
        with self.assertRaises(TypeError):
            r4.width = (5, 8)
        with self.assertRaises(TypeError):
            r4.y = [5, 8, 9]
        with self.assertRaises(ValueError):
            r4.width = -10
        with self.assertRaises(ValueError):
            r4.y = -1
        with self.assertRaises(ValueError):
            r4.height = -7
        with self.assertRaises(ValueError):
            r4.x = -5

    def test_area(self):
        """tests the area of the rectangle object"""
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area2(self):
        """tests the area of the rectangle object"""
        rec = Rectangle(2, 3)
        rec.width = 5
        rec.height = 7
        self.assertEqual(rec.area(), 35)

    def test_display(self):
        """tests the display of the rectangle"""
        r1 = Rectangle(4, 6)
        result = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)
        """test display with x and y"""
        r2 = Rectangle(2, 3, 2, 2)
        result = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r2.display()
            self.assertEqual(str_out.getvalue(), result)

    def test__str__method(self):
        """tests the result of printing the class object"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)
        r2 = Rectangle(5, 5, 1)
        r3 = Rectangle(2, 4)
        result = f"[Rectangle] ({r3.id - 1}) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), result)

    def test__str__(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_update(self):
        """with dict or kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(height=1)
        res = f"[Rectangle] (1) 10/10 - 10/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.update(y=1, width=2, x=3, id=89)
        res = "[Rectangle] (89) 3/1 - 2/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update2(self):
        """without kwargs or dict"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        res = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(r1.__str__(), res)

        r1.update(89)
        res1 = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(r1.__str__(), res1)

        r1.update(89, 2, 3, 4)
        res2 = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(r1.__str__(), res2)

        r1.update(89, 2, 3, 4, 5)
        res3 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(r1.__str__(), res3)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
