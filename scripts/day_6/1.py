"""
Day 6 Part 1: Homework Calculator

This script calculates the total result from a homework assignment
with alternating addition and multiplication operations.
"""

from typing import List, Optional


class Homework:
    """A class to process homework calculations with alternating operations."""

    def __init__(self, input_file: str = "input/day_6.txt"):
        """
        Initialize the Homework processor.

        Args:
            input_file: Path to the input file containing homework data
        """
        self.input_file = input_file

    def read_input(self) -> Optional[List[int]]:
        """
        Read and process the input file to calculate the homework result.

        Returns:
            List of calculated values or None if error occurs
        """
        try:
            with open(self.input_file, "r") as f:
                data = f.readlines()

            if not data:
                print("Error: Input file is empty")
                return None

            # Extract operators from last line
            operators_line = data[-1].replace(" ", "").strip()
            if not operators_line:
                print("Error: No operators found in last line")
                return None

            operators = list(operators_line)
            output = [0 if operator == "+" else 1 for operator in operators]

            # Process each data row
            for row in data[:-1]:
                row_data = row.strip()
                if not row_data:
                    continue

                idx = 0
                for num_str in row_data.split(" "):
                    try:
                        num = int(num_str.strip())
                        if idx < len(operators):
                            if operators[idx] == "+":
                                output[idx] += num
                            else:
                                output[idx] *= num
                            idx += 1
                    except ValueError:
                        continue

            return output

        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found")
            return None
        except Exception as e:
            print(f"Error processing input: {e}")
            return None

    def calculate_total(self) -> None:
        """Calculate and print the total homework result."""
        result = self.read_input()
        if result is not None:
            print(sum(result))


if __name__ == "__main__":
    """Main execution guard."""
    homework = Homework()
    homework.calculate_total()