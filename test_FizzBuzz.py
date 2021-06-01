# Homework 7 test_FizzBuzz.py Alexis Matheson

import unittest

import FizzBuzz


class TestNumber(unittest.TestCase):
    def test_checknum(self):
        self.assertEqual(FizzBuzz.checknum(3), "Fizz")
        self.assertEqual(FizzBuzz.checknum(5), "Buzz")

    def test_checknum(self):
        self.assertEqual(FizzBuzz.checknum(2), 2)


if __name__ == "__main__":
    unittest.main()