"""
Tests for the main module.
"""

import unittest
from unittest.mock import patch
from simple_app.main import greet, main

class TestMain(unittest.TestCase):
    def test_greet(self):
        """Test the greet function with a normal input."""
        result = greet("Test")
        self.assertEqual(result, "Hello, Test! Welcome to SimpleApp!")

    def test_greet_empty_name(self):
        """Test the greet function with an empty name."""
        result = greet("")
        self.assertEqual(result, "Hello, ! Welcome to SimpleApp!")

    def test_greet_special_chars(self):
        """Test the greet function with special characters."""
        result = greet("Test@123")
        self.assertEqual(result, "Hello, Test@123! Welcome to SimpleApp!")

    @patch('builtins.input', return_value='TestUser')
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        """Test the main function with mocked input."""
        main()
        mock_print.assert_called_once_with("Hello, TestUser! Welcome to SimpleApp!")

if __name__ == "__main__":
    unittest.main() 