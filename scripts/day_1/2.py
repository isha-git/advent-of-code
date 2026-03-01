from typing import Tuple
from scripts.day_1.utils import get_new_location


def get_new_location_v2(
    direction: str, delta: int, current: int, upper_limit: int, zero_count: int
) -> Tuple[int, int]:
    """
    Calculate the new location and zero count based on direction and delta.
    
    Args:
        direction: Direction of movement ('L' or 'R').
        delta: Amount to move.
        current: Current position.
        upper_limit: Upper limit for the position.
        zero_count: Current count of zeros encountered.
    
    Returns:
        Tuple of new position and updated zero count.
    """
    if direction == "L":
        if current == 0:
            zero_count += delta // upper_limit
        else:
            zero_count += (delta - current) // upper_limit + 1

        current = (current - delta) % upper_limit

    elif direction == "R":
        if current == 0:
            zero_count += delta // upper_limit
        elif current + delta >= upper_limit:
            zero_count += (delta + current - upper_limit) // upper_limit + 1

        current = (current + delta) % upper_limit

    return current, zero_count


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

        current, zero_count = get_new_location_v2(
            direction, delta, current, upper_limit, zero_count
        )

    return zero_count


if __name__ == "__main__":
    zero_count = get_password()
    print(zero_count)
