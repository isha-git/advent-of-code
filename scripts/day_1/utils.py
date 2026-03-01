from typing import Tuple
import os


def get_new_location(
    direction: str, delta: int, current: int, upper_limit: int, zero_count: int
) -> Tuple[int, int]:
    """Calculate new location based on direction and delta."""
    if direction == "L":
        current = (current - delta) % upper_limit
    elif direction == "R":
        current = (current + delta) % upper_limit

    if current == 0:
        zero_count += 1

    return current, zero_count


def get_new_location_v2(
    direction: str, delta: int, current: int, upper_limit: int, zero_count: int
) -> Tuple[int, int]:
    """Calculate new location with improved zero count logic."""
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


def read_rotations(input_path: str = "input/day_1.txt") -> list:
    """Read and validate rotation instructions from input file."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as f:
        rotations = f.readlines()

    rotations = [r.strip() for r in rotations if r.strip()]
    for rotation in rotations:
        if len(rotation) < 2 or rotation[0] not in ["L", "R"]:
            raise ValueError(f"Invalid rotation format: {rotation}")
        try:
            int(rotation[1:])
        except ValueError:
            raise ValueError(f"Invalid delta value: {rotation[1:]}")

    return rotations


def calculate_password(rotations: list, start: int = 50, upper_limit: int = 100, version: int = 1) -> int:
    """Calculate password based on rotation instructions."""
    current = start
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]
        delta = int(rotation[1:])

        if version == 1:
            current, zero_count = get_new_location(
                direction, delta, current, upper_limit, zero_count
            )
        else:
            current, zero_count = get_new_location_v2(
                direction, delta, current, upper_limit, zero_count
            )

    return zero_count