#!/usr/bin/env python3
from ubuntu import prependHome
import unittest

class TestStuff(unittest.TestCase):
    def test_home(self):
        self.assertEqual(prependHome(""), "/home/sparib/")

if __name__ == "__main__":
    unittest.main()
