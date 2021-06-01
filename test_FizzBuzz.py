# Homework 7 test_FizzBuzz.py Alexis Matheson

import unittest

# import FizzBuzz


class TestNumber(unittest.TestCase):
    def test_checknum(self):
        self.assertEqual(FizzBuzz.checknum(3), "Buzz")


if __name__ == "__main__":
    unittest.main()