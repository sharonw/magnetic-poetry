"""
Test cases for noteworthy lines from Mean Girls.
"""

import unittest

class SecretsTest(unittest.TestCase):
    def test(self):
        self.assertFalse("That's why her hair is so big, it's full of secrets.")

class ShoppingTest(unittest.TestCase):
    def test(self):
        self.assertFalse("Get in loser, we're going shopping.")

class AfricaTest(unittest.TestCase):
    def test(self):
        self.assertFalse("If you're from Africa, why are you white?")

class PinkTest(unittest.TestCase):
    def test(self):
        self.assertFalse("On Wednesdays we wear pink!")

class MartianTest(unittest.TestCase):
    def test(self):
        self.assertFalse("I love her. She's like a Martian!")

if __name__ == '__main__':
    unittest.main()
