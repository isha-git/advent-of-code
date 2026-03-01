from scripts.day_1.utils import read_rotations, calculate_password


def get_password() -> int:
    """Calculate password using version 2 logic."""
    rotations = read_rotations()
    return calculate_password(rotations, version=2)


if __name__ == "__main__":
    zero_count = get_password()
    print(zero_count)