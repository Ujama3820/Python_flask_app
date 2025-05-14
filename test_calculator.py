import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        print("Testing addition")
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        print("Testing Subtraction")
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        print("Testing Multiplication")
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        print("Testing division")
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide_by_zero(self):
        print("Testing division by zero")
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
