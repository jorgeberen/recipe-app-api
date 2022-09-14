""""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding number together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(11, 5)
        self.assertEqual(res, 6)
