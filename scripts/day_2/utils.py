import os
from typing import List, Tuple, Set


def read_ids(input_path: str = "input/day_2.txt") -> List[str]:
    """Read and validate IDs from input file."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as f:
        ids = f.readlines()

    if not ids:
        raise ValueError("Input file is empty")

    ids = ids[0].strip().split(",")
    for id in ids:
        if "-" not in id:
            raise ValueError(f"Invalid ID format: {id}")
        left, right = id.split("-")
        try:
            int(left)
            int(right)
        except ValueError:
            raise ValueError(f"Invalid numeric value in ID: {id}")

    return ids


def find_invalid_v1(left: str, right: str) -> int:
    """Find invalid numbers using version 1 logic."""
    left_length = len(left)
    right_length = len(right)

    if left_length % 2 != 0:
        left = "1" + "0" * left_length
        if int(left) > int(right):
            return 0

    if right_length % 2 != 0:
        right = "1" + "0" * (right_length - 1)
        if int(right) < int(left):
            return 0

    left_length = len(left)
    right_length = len(right)

    left_left_chunk = left[: int(left_length / 2)]
    diff = int((int(right) - int(left)) // 2)

    invalid_count = 0
    for i in range(diff):
        new_num = int(left_left_chunk * 2)
        if (new_num >= int(left)) and (new_num <= int(right)):
            invalid_count += new_num
        left_left_chunk = str(int(left_left_chunk) + 1)

    return invalid_count


def possible_invalid_length(number_length: int) -> List[int]:
    """Find possible invalid lengths for a number."""
    possible_lengths = []
    for i in range(1, int(number_length)):
        if number_length % i == 0:
            possible_lengths.append(i)
    return possible_lengths


def find_invalid_v2(left: str, right: str) -> Set[int]:
    """Find invalid numbers using version 2 logic."""
    invalid_values = set()

    chunk_sizes = [len(left)]
    curr_num = left
    while True:
        chunk_size = len(curr_num) + 1
        if chunk_size > len(right):
            break
        else:
            chunk_sizes.append(chunk_size)
        curr_num = "1" + curr_num

    for chunk_size in chunk_sizes:
        possible_lengths = possible_invalid_length(chunk_size)
        for pattern_length in possible_lengths:
            upper_limit = int("9" * pattern_length)
            for i in range(1, upper_limit + 1):
                new_num = int(str(i) * (chunk_size // pattern_length))
                if new_num > int(right):
                    break
                if (new_num >= int(left)) and (new_num <= int(right)):
                    invalid_values.add(new_num)

    return invalid_values


def calculate_invalid_total(ids: List[str], version: int = 1) -> int:
    """Calculate total invalid numbers for all ID ranges."""
    invalid_total = 0

    for id in ids:
        left, right = id.split("-")
        if version == 1:
            invalid_total += find_invalid_v1(left, right)
        else:
            invalid_values = find_invalid_v2(left, right)
            if invalid_values:
                for val in invalid_values:
                    invalid_total += int(val)

    return invalid_total