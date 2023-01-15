#!/usr/bin/python3

"""Module for unit testing for the Base class"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """unit test case for the base class"""

    def test_default_id(self):
        """test default id for the object"""
        bs = Base()
        bs1 = Base()
        self.assertEqual(bs.id, bs1.id - 1)

    def test_id(self):
        """test id with argument"""
        bs = Base(9)
        self.assertEqual(bs.id, 9)

    def test_different_id(self):
        """test different id with more objects created"""
        bs1 = Base()
        bs2 = Base()
        bs3 = Base(5)
        bs4 = Base()
        bs5 = Base()
        self.assertEqual(bs1.id, bs2.id - 1)
        self.assertEqual(bs2.id, bs4.id - 1)
        self.assertEqual(bs4.id, bs5.id - 1)
        self.assertEqual(bs3.id, 5)

    def test_two_args(self):
        """test class call with two arguments"""
        with self.assertRaises(TypeError):
            bs = Base(1, 2)

    def test_None(self):
        """test none argument"""
        bs = Base(None)
        bs1 = Base(None)
        self.assertEqual(bs.id, bs1.id - 1)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
            
    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
