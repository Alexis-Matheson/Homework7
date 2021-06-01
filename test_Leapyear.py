# Homework 7 test_Leapyear.py Alexis Matheson

import unittest

# import Leapyear


class TestNumber(unittest.TestCase):
    def test_leapyear(self):
        self.assertEqual(Leapyear.checkyear(2000), False)


if __name__ == "__main__":
    unittest.main()