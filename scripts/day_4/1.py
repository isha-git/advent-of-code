class PaperRoll:
    def __init__(self):
        self.num_of_rows = 0
        self.num_of_cols = 0
        self.grid = []
        self.count = 0

    def get_count(self):
        for row in range(1, self.num_of_rows + 1):
            for col in range(1, self.num_of_cols + 1):
                curr_count = 0
                curr = self.grid[row][col]
                if curr == 1:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            curr_count += self.grid[row + i][col + j]

                    curr_count -= curr

                    if curr_count < 4:
                        self.count += 1

    def read_input(self):
        with open("input/day_4.txt", "r") as f:
            rolls = f.readlines()

        self.num_of_rows = len(rolls)
        self.num_of_cols = len(rolls[0].strip())

        self.grid = [
            [0 for _ in range(self.num_of_cols + 2)]
            for _ in range(self.num_of_rows + 2)
        ]

        for row, roll in enumerate(rolls):
            roll = roll.strip()
            for col, val in enumerate(roll):
                if val == ".":
                    self.grid[row + 1][col + 1] = 0
                else:
                    self.grid[row + 1][col + 1] = 1

    def forklift(self):
        self.read_input()
        self.get_count()
        print(self.count)


PaperRoll().forklift()
