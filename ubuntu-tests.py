#!/usr/bin/env python3
from ubuntu import prependHome, execute
import unittest
from unittest.mock import patch

class TestStuff(unittest.TestCase):
    def test_home(self):
        self.assertEqual(prependHome(""), "/home/sparib/")

    @patch('builtins.input', return_value="n")
    def test_no(self, _):
        self.assertEqual(execute("test_command"), None)

    @patch('builtins.input', return_value="y")
    def test_yes(self, _):
        self.assertEqual(execute("echo", "test"), "test\n")


if __name__ == "__main__":
    unittest.main()
