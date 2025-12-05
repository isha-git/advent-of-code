import copy


class PaperRoll:
    def __init__(self):
        self.num_of_rows = 0
        self.num_of_cols = 0
        self.count = 0

    def get_count(self, grid) -> list[list[int]]:
        new_grid = copy.deepcopy(grid)
        for row in range(1, self.num_of_rows + 1):
            for col in range(1, self.num_of_cols + 1):
                curr_count = 0
                curr = grid[row][col]
                if curr == 1:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            curr_count += grid[row + i][col + j]

                    curr_count -= curr

                    if curr_count < 4:
                        self.count += 1
                        new_grid[row][col] = 0

        return new_grid

    def read_input(self) -> list[list[int]]:
        with open("input/day_4.txt", "r") as f:
            rolls = f.readlines()

        self.num_of_rows = len(rolls)
        self.num_of_cols = len(rolls[0].strip())

        grid = [
            [0 for _ in range(self.num_of_cols + 2)]
            for _ in range(self.num_of_rows + 2)
        ]

        for row, roll in enumerate(rolls):
            roll = roll.strip()
            for col, val in enumerate(roll):
                if val == ".":
                    grid[row + 1][col + 1] = 0
                else:
                    grid[row + 1][col + 1] = 1

        return grid

    def forklift(self):
        grid = self.read_input()
        new_grid = []
        while True:
            new_grid = self.get_count(grid)
            if new_grid == grid:
                break
            grid = copy.deepcopy(new_grid)

        print(self.count)


PaperRoll().forklift()
