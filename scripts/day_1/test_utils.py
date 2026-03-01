"""
Test cases for the Day 1 utility functions.
"""
import unittest
from scripts.day_1.utils import get_new_location


class TestGetNewLocation(unittest.TestCase):
    """Test cases for the get_new_location function."""

    def test_left_rotation_no_zero(self):
        """Test left rotation without crossing zero."""
        current, zero_count = get_new_location("L", 10, 50, 100, 0)
        self.assertEqual(current, 40)
        self.assertEqual(zero_count, 0)

    def test_left_rotation_cross_zero(self):
        """Test left rotation crossing zero."""
        current, zero_count = get_new_location("L", 60, 50, 100, 0)
        self.assertEqual(current, 90)
        self.assertEqual(zero_count, 1)

    def test_right_rotation_no_zero(self):
        """Test right rotation without crossing zero."""
        current, zero_count = get_new_location("R", 10, 50, 100, 0)
        self.assertEqual(current, 60)
        self.assertEqual(zero_count, 0)

    def test_right_rotation_cross_zero(self):
        """Test right rotation crossing zero."""
        current, zero_count = get_new_location("R", 60, 50, 100, 0)
        self.assertEqual(current, 10)
        self.assertEqual(zero_count, 1)

    def test_invalid_direction(self):
        """Test invalid direction handling."""
        current, zero_count = get_new_location("X", 10, 50, 100, 0)
        self.assertEqual(current, 50)
        self.assertEqual(zero_count, 0)


if __name__ == "__main__":
    unittest.main()