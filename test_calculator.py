import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(-5, 4), -1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 4), 1)
        self.assertEqual(sub(-5, 4), -9)
        self.assertEqual(sub(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(5, 4), 20)
        self.assertEqual(mul(-5, 4), -20)
        self.assertEqual(mul(0, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(5, 4), 0.8)
        self.assertAlmostEqual(div(-5, 4), -0.8)
        self.assertEqual(div(2, 10), 5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(27, 3), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 10), 10)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()