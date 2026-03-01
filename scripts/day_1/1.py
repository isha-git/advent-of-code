from typing import Tuple
from scripts.day_1.utils import get_new_location


def get_password() -> int:
    """
    Calculate the password based on rotations in the input file.
    
    Returns:
        Count of zeros encountered during rotations.
    """
    start = 50
    current = start
    upper_limit = 100
    zero_count = 0

    try:
        with open("input/day_1.txt", "r") as f:
            rotations = f.readlines()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1

    for rotation in rotations:
        try:
            direction = rotation[0]
            delta = int(rotation[1:])
        except (IndexError, ValueError) as e:
            print(f"Error parsing rotation: {e}")
            continue

        current, zero_count = get_new_location(
            direction, delta, current, upper_limit, zero_count
        )

    return zero_count


if __name__ == "__main__":
    zero_count = get_password()
    print(zero_count)
