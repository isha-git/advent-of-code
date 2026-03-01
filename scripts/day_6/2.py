"""
Day 6 Part 2: Advanced Homework Calculator

This script calculates the total result from a homework assignment
with alternating addition and multiplication operations, handling
multi-digit numbers across columns.
"""

import math
import numpy as np
from typing import Tuple, List, Optional, Union


class Homework:
    """A class to process advanced homework calculations with multi-digit numbers."""

    def __init__(self, input_file: str = "input/day_6.txt"):
        """
        Initialize the Homework processor.

        Args:
            input_file: Path to the input file containing homework data
        """
        self.input_file = input_file

    def read_input(self) -> Tuple[Optional[np.ndarray], Optional[List[str]]]:
        """
        Read and parse the input file into a matrix and operators list.

        Returns:
            Tuple containing (input_matrix, operators) or (None, None) if error occurs
        """
        try:
            with open(self.input_file, "r") as f:
                data = f.readlines()

            if len(data) < 2:
                print("Error: Input file must contain at least 2 lines")
                return None, None

            # Extract operators from last line
            operators_line = data[-1].replace(" ", "").strip()
            if not operators_line:
                print("Error: No operators found in last line")
                return None, None

            operators = list(operators_line)
            data_rows = data[:-1]

            # Create input matrix
            max_length = max(len(row.strip("\n")) for row in data_rows)
            input_matrix = np.zeros((len(data_rows), max_length), dtype="O")

            for idx, row in enumerate(data_rows):
                row_data = row.strip("\n")
                if len(row_data) < max_length:
                    row_data = row_data.ljust(max_length)
                input_matrix[idx] = list(row_data)

            return input_matrix, operators

        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found")
            return None, None
        except Exception as e:
            print(f"Error processing input: {e}")
            return None, None

    def get_total(self, input_matrix: np.ndarray, operators: List[str]) -> int:
        """
        Calculate the total result from the input matrix and operators.

        Args:
            input_matrix: 2D numpy array containing the input data
            operators: List of operators ('+' or '*')

        Returns:
            Calculated total result
        """
        if input_matrix.size == 0 or not operators:
            return 0

        output = 0
        curr_idx = 0
        operator_idx = 0
        curr_num_list = []

        while curr_idx < input_matrix.shape[1]:
            # Check if current column is all spaces (separator)
            if all(row[curr_idx] == " " for row in input_matrix):
                if curr_num_list and operator_idx < len(operators):
                    if operators[operator_idx] == "+":
                        output += sum(curr_num_list)
                    else:
                        output += math.prod(curr_num_list)
                    operator_idx += 1
                    curr_num_list = []
            else:
                # Extract number from current column
                curr_num = "".join(input_matrix[:, curr_idx])
                try:
                    curr_num_list.append(int(curr_num))
                except ValueError:
                    pass

            curr_idx += 1

            # Handle end of matrix
            if curr_idx == input_matrix.shape[1] and curr_num_list:
                if operator_idx < len(operators):
                    if operators[operator_idx] == "+":
                        output += sum(curr_num_list)
                    else:
                        output += math.prod(curr_num_list)

        return output

    def calculate_grand_total(self) -> None:
        """Calculate and print the grand total homework result."""
        try:
            input_matrix, operators = self.read_input()
            if input_matrix is not None and operators is not None:
                output = self.get_total(input_matrix, operators)
                print(output)
        except Exception as e:
            print(f"Error calculating grand total: {e}")


if __name__ == "__main__":
    """Main execution guard."""
    homework = Homework()
    homework.calculate_grand_total()