class Ingredients:
    def __init__(self):
        self.fresh_count = 0
        self.fresh_range = {}

    def is_fresh(self, id):
        for left, right in self.fresh_range.items():
            if id >= left:
                if id <= right:
                    self.fresh_count += 1
                    break

    def read_input(self):
        with open("input/day_5.txt", "r") as f:
            data = f.readlines()

        ids = []
        flag = True
        for row in data:
            if row == "\n":
                flag = False
                continue
            if flag:
                left, right = map(int, row.strip().split("-"))
                if left in self.fresh_range.keys():
                    self.fresh_range[left] = max(right, self.fresh_range[left])
                else:
                    self.fresh_range[left] = right
            else:
                ids.append(int(row.strip()))

        return ids

    def get_fresh_count(self):
        ids = self.read_input()
        for id in ids:
            self.is_fresh(id)

        print(self.fresh_count)


Ingredients().get_fresh_count()
