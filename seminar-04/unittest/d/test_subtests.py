import unittest

from factorial import factorial as fact
from math import factorial as mfact


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 3 are all even.
        """
        for i in range(0, 4):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(fact(i), mfact(i))


if __name__ == '__main__':
    unittest.main()
