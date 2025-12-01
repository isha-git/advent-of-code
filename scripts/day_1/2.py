from typing import Tuple


def get_new_location(
    direction: str, delta: int, current: int, upper_limit: int, zero_count: int
) -> Tuple[int, int]:
    if direction == "L":
        if current == 0:
            zero_count += delta // 100
        else:
            zero_count += (delta - current) // 100 + 1

        current = (current - delta) % 100

    elif direction == "R":
        if current == 0:
            zero_count += delta // 100
        elif current + delta >= 100:
            zero_count += (delta + current - 100) // 100 + 1

        current = (current + delta) % 100

    return current, zero_count


def get_password():
    start = 50
    current = start
    upper_limit = 100
    zero_count = 0

    with open("input/day_1.txt", "r") as f:
        rotations = f.readlines()

    for rotation in rotations:
        direction = rotation[0]
        delta = int(rotation[1:])

        current, zero_count = get_new_location(
            direction, delta, current, upper_limit, zero_count
        )

    return zero_count


if __name__ == "__main__":
    zero_count = get_password()
    print(zero_count)
