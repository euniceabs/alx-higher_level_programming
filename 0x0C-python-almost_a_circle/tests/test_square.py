#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


import unittest
from models.square import Square

class SquareTestCase(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def tearDown(self):
        del self.square

    def test_square_instantiation(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_square_str(self):
        self.assertEqual(
            str(self.square),
            "[Square] (1) 2/3 - 5"
        )

    def test_square_update_args(self):
        self.square.update(2, 8, 4, 7)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 7)

    def test_square_update_kwargs(self):
        self.square.update(x=5, y=6, size=7)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 6)
        self.assertEqual(self.square.size, 7)

    def test_square_to_dictionary(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertDictEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
