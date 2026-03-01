"""
Test cases for file handling in Day 1 scripts.
"""
import unittest
import os
from unittest.mock import patch, mock_open
from scripts.day_1 import 1


class TestFileHandling(unittest.TestCase):
    """Test cases for file handling in Day 1 scripts."""

    def test_file_not_found(self):
        """Test handling of missing input file."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = 1.get_password()
            self.assertEqual(result, -1)

    def test_file_read_error(self):
        """Test handling of file read errors."""
        with patch("builtins.open", side_effect=Exception("Read error")):
            result = 1.get_password()
            self.assertEqual(result, -1)

    def test_invalid_rotation_format(self):
        """Test handling of invalid rotation format."""
        mock_data = ["X10\n", "Invalid\n"]
        with patch("builtins.open", mock_open(read_data="\n".join(mock_data))):
            result = 1.get_password()
            self.assertEqual(result, 0)

    def test_valid_rotations(self):
        """Test handling of valid rotations."""
        mock_data = ["L10\n", "R20\n"]
        with patch("builtins.open", mock_open(read_data="\n".join(mock_data))):
            result = 1.get_password()
            self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()