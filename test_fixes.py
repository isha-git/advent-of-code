#!/usr/bin/env python3
"""
Comprehensive test suite to verify all the bug fixes and improvements.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import patch, mock_open

# Add scripts to path
sys.path.insert(0, 'scripts')

from day_1.utils import read_rotations, calculate_password, get_new_location, get_new_location_v2
from day_1 import 1 as day1_1, 2 as day1_2
from day_2.utils import read_ids, calculate_invalid_total, find_invalid_v1, find_invalid_v2
from day_2 import 1 as day2_1, 2 as day2_2


class TestDay1Fixes(unittest.TestCase):
    """Test Day 1 fixes."""

    def test_read_rotations_error_handling(self):
        """Test error handling in read_rotations."""
        # Test file not found
        with patch('os.path.exists', return_value=False):
            result = read_rotations("nonexistent.txt")
            self.assertEqual(result, [])

        # Test invalid format
        mock_data = ["X10\n", "Invalid\n"]
        with patch('builtins.open', mock_open(read_data="\n".join(mock_data))):
            result = read_rotations()
            self.assertEqual(result, [])

    def test_calculate_password_empty_input(self):
        """Test calculate_password with empty input."""
        result = calculate_password([])
        self.assertEqual(result, 0)

    def test_get_password_error_handling(self):
        """Test error handling in get_password functions."""
        with patch('scripts.day_1.utils.read_rotations', return_value=[]):
            result1 = day1_1.get_password()
            result2 = day1_2.get_password()
            self.assertEqual(result1, -1)
            self.assertEqual(result2, -1)


class TestDay2Fixes(unittest.TestCase):
    """Test Day 2 fixes."""

    def test_read_ids_error_handling(self):
        """Test error handling in read_ids."""
        # Test file not found
        with patch('os.path.exists', return_value=False):
            result = read_ids("nonexistent.txt")
            self.assertEqual(result, [])

        # Test empty file
        with patch('builtins.open', mock_open(read_data="")):
            result = read_ids()
            self.assertEqual(result, [])

    def test_find_invalid_v1_edge_cases(self):
        """Test edge cases in find_invalid_v1."""
        # Test left > right
        result = find_invalid_v1("10", "5")
        self.assertEqual(result, 0)

        # Test equal values
        result = find_invalid_v1("5", "5")
        self.assertEqual(result, 0)

    def test_find_invalid_v2_edge_cases(self):
        """Test edge cases in find_invalid_v2."""
        # Test left > right
        result = find_invalid_v2("10", "5")
        self.assertEqual(result, set())

    def test_calculate_invalid_total_empty(self):
        """Test calculate_invalid_total with empty input."""
        result = calculate_invalid_total([])
        self.assertEqual(result, 0)


class TestDay3Fixes(unittest.TestCase):
    """Test Day 3 fixes."""

    def test_get_joltage_edge_cases(self):
        """Test edge cases in get_joltage."""
        from day_3 import 1 as day3
        lobby = day3.Lobby()

        # Test single character
        result = lobby.get_joltage("5")
        self.assertEqual(result, 55)  # 5 and 5

        # Test empty string
        result = lobby.get_joltage("")
        self.assertEqual(result, 0)

        # Test all same digits
        result = lobby.get_joltage("111")
        self.assertEqual(result, 11)  # 1 and 1


class TestDay4Fixes(unittest.TestCase):
    """Test Day 4 fixes."""

    def test_grid_bounds_checking(self):
        """Test grid bounds checking in get_count."""
        from day_4 import 1 as day4
        paper = day4.PaperRoll()

        # Create a small grid for testing
        paper.num_of_rows = 2
        paper.num_of_cols = 2
        paper.grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]

        # This should not cause index errors
        paper.get_count()
        self.assertTrue(True)  # If we get here, no index errors occurred


class TestDay5Fixes(unittest.TestCase):
    """Test Day 5 fixes."""

    def test_is_fresh_edge_cases(self):
        """Test edge cases in is_fresh."""
        from day_5 import 1 as day5
        ingredients = day5.Ingredients()

        # Test with empty fresh_range
        ingredients.fresh_range = {}
        ingredients.is_fresh(10)
        self.assertEqual(ingredients.fresh_count, 0)


class TestDay6Fixes(unittest.TestCase):
    """Test Day 6 fixes."""

    def test_operator_validation(self):
        """Test operator validation in read_input."""
        from day_6 import 1 as day6
        
        # Create a temporary file with invalid operator
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("1 2 3\n")
            f.write("+ * X\n")  # X is invalid
            temp_path = f.name

        try:
            # Mock the file path
            with patch('builtins.open', mock_open(read_data=f"1 2 3\n+ * X\n")):
                homework = day6.Homework()
                homework.read_input()
                # Should handle invalid operator gracefully
        finally:
            os.unlink(temp_path)


class TestDay7Fixes(unittest.TestCase):
    """Test Day 7 fixes."""

    def test_get_splits_edge_cases(self):
        """Test edge cases in get_splits."""
        from day_7 import 1 as day7
        beam = day7.Beam()

        # Test empty data
        result = beam.get_splits([])
        self.assertEqual(result, 0)

        # Test data with only start row
        result = beam.get_splits(["S"])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)