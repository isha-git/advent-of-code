from scripts.day_2.utils import read_ids, calculate_invalid_total


class GiftShop:
    def __init__(self):
        self.invalid_total = 0

    def find_total(self):
        """Calculate total invalid numbers using version 2 logic."""
        ids = read_ids()
        self.invalid_total = calculate_invalid_total(ids, version=2)
        print("Invalid total:", self.invalid_total)


if __name__ == "__main__":
    GiftShop().find_total()