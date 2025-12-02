class GiftShop:
    def __init__(self):
        self.input_path = "input/day_2.txt"
        self.invalid_count = 0

    def find_invalid(self, left: str, right: str):
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

        for i in range(diff):
            new_num = int(left_left_chunk * 2)
            if (new_num >= int(left)) and (new_num <= int(right)):
                self.invalid_count += new_num
            left_left_chunk = str(int(left_left_chunk) + 1)

    def read_input(self) -> list:
        with open(self.input_path, "r") as f:
            ids = f.readlines()

        ids = ids[0].split(",")
        return ids

    def find_total(self):
        ids = self.read_input()
        for id in ids:
            left, right = id.split("-")
            self.find_invalid(left, right)

        print(self.invalid_count)


GiftShop().find_total()
