"""
Tests for the main module.
"""

import unittest
from simple_app.main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        """Test the greet function."""
        result = greet("Test")
        self.assertEqual(result, "Hello, Test! Welcome to SimpleApp!")

if __name__ == "__main__":
    unittest.main() 