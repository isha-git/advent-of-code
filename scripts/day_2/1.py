from scripts.day_2.utils import read_ids, calculate_invalid_total


class GiftShop:
    def __init__(self):
        self.invalid_count = 0

    def find_total(self):
        """Calculate total invalid numbers using version 1 logic."""
        ids = read_ids()
        self.invalid_count = calculate_invalid_total(ids, version=1)
        print(self.invalid_count)


if __name__ == "__main__":
    GiftShop().find_total()