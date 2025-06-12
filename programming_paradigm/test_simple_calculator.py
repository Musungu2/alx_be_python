import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(6, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()

