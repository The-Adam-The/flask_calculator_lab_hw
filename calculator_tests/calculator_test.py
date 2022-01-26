from modules.calculator import add, subtract, multiply, divide
import unittest

class CalculatorTest(unittest.TestCase):

    def test_calc_adds_numbers(self):
        self.assertEqual(10, add(5, 5))

    def test_calc_subtracts_numbers(self):
        self.assertEqual(5, subtract(10,5))

    def test_calc_multiplys_numbers(self):
        self.assertEqual(25, multiply(5, 5))

    def test_calc_divides_numbers(self):
        self.assertEqual(5, divide(25, 5))