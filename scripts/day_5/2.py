class Ingredients:
    def __init__(self):
        self.input_range = {}
        self.final_range = {}

    def fresh_count(self) -> int:
        fresh_count = 0
        for left, right in self.final_range.items():
            fresh_count += right - left + 1

        return fresh_count

    def fresh_list(self):
        left = sorted(self.input_range.keys())

        idx = 0
        while True:
            if left[idx] in self.final_range.keys():
                curr_right = self.final_range[left[idx]]
            else:
                curr_right = self.input_range[left[idx]]
            next_right = self.input_range[left[idx + 1]]
            if curr_right >= left[idx + 1]:
                self.final_range[left[idx]] = max(curr_right, next_right)
                left.pop(idx + 1)

                if idx == len(left) - 1:
                    break
            else:
                self.final_range[left[idx]] = curr_right
                idx += 1
                if idx == len(left) - 1:
                    self.final_range[left[idx]] = self.input_range[left[idx]]
                    break

    def read_input(self):
        with open("input/day_5.txt", "r") as f:
            data = f.readlines()

        for row in data:
            if row == "\n":
                break
            left, right = map(int, row.strip().split("-"))
            if left in self.input_range.keys():
                self.input_range[left] = max(right, self.input_range[left])
            else:
                self.input_range[left] = right

    def get_fresh_count(self):
        self.read_input()
        self.fresh_list()
        fresh_count = self.fresh_count()

        print(fresh_count)


Ingredients().get_fresh_count()
