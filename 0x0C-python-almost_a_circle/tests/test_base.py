#!/usr/bin/python3
"""unittests definition for base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(10, 7, 2, 8, 5)
        self.s = Square(10, 2, 3, 4)

    def tearDown(self):
        del self.r
        del self.s

    def test_base_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_base_to_json_string_rectangle(self):
        json_string = Base.to_json_string([self.r.to_dictionary()])
        self.assertIsInstance(json_string, str)

    def test_base_to_json_string_square(self):
        json_string = Base.to_json_string([self.s.to_dictionary()])
        self.assertIsInstance(json_string, str)

    def test_base_save_to_file_rectangle(self):
        Rectangle.save_to_file([self.r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_base_save_to_file_square(self):
        Square.save_to_file([self.s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_base_from_json_string_rectangle(self):
        json_string = Base.to_json_string([self.r.to_dictionary()])
        objects = Rectangle.from_json_string(json_string)
        self.assertEqual(len(objects), 1)
        new_r = Rectangle.create(**objects[0])
        self.assertEqual(new_r.id, self.r.id)
        self.assertEqual(new_r.width, self.r.width)
        self.assertEqual(new_r.height, self.r.height)
        self.assertEqual(new_r.x, self.r.x)
        self.assertEqual(new_r.y, self.r.y)

    def test_base_from_json_string_square(self):
        json_string = Base.to_json_string([self.s.to_dictionary()])
        objects = Square.from_json_string(json_string)
        self.assertEqual(len(objects), 1)
        new_s = Square.create(**objects[0])
        self.assertEqual(new_s.size, self.s.size)
        self.assertEqual(new_s.x, self.s.x)
        self.assertEqual(new_s.y, self.s.y)


    def test_base_create_rectangle(self):
        new_r = Rectangle.create(**self.r.to_dictionary())
        self.assertEqual(str(new_r), str(self.r))

    def test_base_create_square(self):
        new_s = Square.create(**self.s.to_dictionary())
        self.assertEqual(str(new_s), str(self.s))

    def test_base_load_from_file_rectangle(self):
        Rectangle.save_to_file([self.r])
        objects = Rectangle.load_from_file()
        self.assertEqual(len(objects), 1)
        self.assertIsInstance(objects[0], Rectangle)

    def test_base_load_from_file_square(self):
        Square.save_to_file([self.s])
        objects = Square.load_from_file()
        self.assertEqual(len(objects), 1)
        self.assertIsInstance(objects[0], Square)


if __name__ == "__main__":
    unittest.main()
