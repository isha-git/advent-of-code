from typing import Tuple


def get_new_location(
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
        current = (current - delta) % upper_limit
    elif direction == "R":
        current = (current + delta) % upper_limit
    
    if current == 0:
        zero_count += 1
    
    return current, zero_count
