"""
Test cases for Day 1 utility functions.
"""
import unittest
from utils import read_rotations, get_new_location, calculate_password


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_read_rotations(self):
        """Test reading rotations from a file."""
        with open("test_input.txt", "w") as file:
            file.write("10\n20\n30\n")
        
        rotations = read_rotations("test_input.txt")
        self.assertEqual(rotations, [10, 20, 30])

    def test_read_rotations_invalid(self):
        """Test reading rotations with invalid data."""
        with open("test_input.txt", "w") as file:
            file.write("10\nabc\n30\n")
        
        with self.assertRaises(ValueError):
            read_rotations("test_input.txt")

    def test_read_rotations_non_positive(self):
        """Test reading rotations with non-positive delta."""
        with open("test_input.txt", "w") as file:
            file.write("10\n-5\n30\n")
        
        with self.assertRaises(ValueError):
            read_rotations("test_input.txt")

    def test_get_new_location_v1(self):
        """Test get_new_location for version 1."""
        new_location, zero_count = get_new_location(50, 50, version=1)
        self.assertEqual(new_location, 0)
        self.assertEqual(zero_count, 1)

    def test_get_new_location_v2(self):
        """Test get_new_location for version 2."""
        new_location, zero_count = get_new_location(50, 50, version=2)
        self.assertEqual(new_location, 0)
        self.assertEqual(zero_count, 2)

    def test_calculate_password_v1(self):
        """Test calculate_password for version 1."""
        rotations = [50, 50]
        password = calculate_password(rotations, version=1)
        self.assertEqual(password, 100)

    def test_calculate_password_v2(self):
        """Test calculate_password for version 2."""
        rotations = [50, 50]
        password = calculate_password(rotations, version=2)
        self.assertEqual(password, 200)


if __name__ == "__main__":
    unittest.main()
