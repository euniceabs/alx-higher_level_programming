#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


import unittest
from models.rectangle import Rectangle

class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 10, 2, 3, 1)

    def tearDown(self):
        del self.rect

    def test_rectangle_instantiation(self):
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_rectangle_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_rectangle_str(self):
        self.assertEqual(
            str(self.rect),
            "[Rectangle] (1) 2/3 - 5/10"
        )

    def test_rectangle_update_args(self):
        self.rect.update(2, 8, 6, 4, 7)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 7)

    def test_rectangle_update_kwargs(self):
        self.rect.update(x=5, y=6, width=7, height=8)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 6)
        self.assertEqual(self.rect.width, 7)
        self.assertEqual(self.rect.height, 8)

    def test_rectangle_to_dictionary(self):
        rect_dict = self.rect.to_dictionary()
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertDictEqual(rect_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
