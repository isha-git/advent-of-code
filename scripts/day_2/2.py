class GiftShop:
    def __init__(self):
        self.input_path = "input/day_2.txt"
        self.invalid_total = 0

    def possible_invalid_length(self, number_length):
        possible_lengths = []
        for i in range(1, int(number_length)):
            if number_length % i == 0:
                possible_lengths.append(i)

        return possible_lengths

    def find_invalid(self, left: str, right: str):
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
            possible_lengths = self.possible_invalid_length(chunk_size)
            for pattern_length in possible_lengths:
                upper_limit = int("9" * pattern_length)
                for i in range(1, upper_limit + 1):
                    new_num = int(str(i) * (chunk_size // pattern_length))
                    if new_num > int(right):
                        break
                    if (new_num >= int(left)) and (new_num <= int(right)):
                        invalid_values.add(new_num)

        return invalid_values

    def read_input(self) -> list:
        with open(self.input_path, "r") as f:
            ids = f.readlines()

        ids = ids[0].split(",")
        return ids

    def find_total(self):
        ids = self.read_input()
        for id in ids:
            left, right = id.split("-")
            invalid_values = self.find_invalid(left, right)

            if invalid_values:
                for val in invalid_values:
                    self.invalid_total += int(val)
        print("Invalid total:", self.invalid_total)


GiftShop().find_total()
