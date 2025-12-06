import math
import numpy as np
from typing import Tuple


class Homework:
    def get_total(self, input_matrix: list[list], operators: list) -> int:
        output = 0
        curr_idx = 0
        operator_idx = 0
        curr_num_list = []
        while curr_idx < input_matrix.shape[1]:
            if all(row[curr_idx] == " " for row in input_matrix):
                if operators[operator_idx] == "+":
                    output += sum(curr_num_list)
                else:
                    output += math.prod(curr_num_list)
                operator_idx += 1
                curr_num_list = []
            else:
                curr_num = "".join(input_matrix[:, curr_idx])
                curr_num_list.append(int(curr_num))

            curr_idx += 1
            if curr_idx == (input_matrix.shape[1] - 1):
                curr_num = "".join(input_matrix[:, curr_idx])
                curr_num_list.append(int(curr_num))
                if operators[operator_idx] == "+":
                    output += sum(curr_num_list)
                else:
                    output += math.prod(curr_num_list)

        return output

    def read_input(self) -> Tuple[list[list], list]:
        with open("input/day_6.txt", "r") as f:
            data = f.readlines()

        operators = list(data[-1].replace(" ", "").strip())
        data = data[:-1]
        input_matrix = np.zeros((len(data), len(data[0].strip("\n"))), dtype="O")

        for idx, row in enumerate(data):
            input_matrix[idx] = list(row.strip("\n"))

        input_matrix = np.array(input_matrix)

        return input_matrix, operators

    def grand_total(self):
        input_matrix, operators = self.read_input()
        output = self.get_total(input_matrix, operators)

        print(output)


Homework().grand_total()
