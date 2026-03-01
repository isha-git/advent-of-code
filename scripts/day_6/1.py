class Homework:
    def __init__(self):
        pass

    def read_input(self):
        """
        Read input from the file and calculate the output.
        """
        try:
            with open("input/day_6.txt", "r") as f:
                data = f.readlines()

            if not data:
                print("Error: Empty input file.")
                return

            operators = list(data[-1].replace(" ", "").strip())
            output = [0 if operator == "+" else 1 for operator in operators]

            for row in data[:-1]:
                idx = 0
                for num in row.strip().split(" "):
                    try:
                        num = int(num.strip())
                        if operators[idx] == "+":
                            output[idx] += num
                        else:
                            output[idx] *= num
                        idx += 1
                    except Exception:
                        continue

            print(sum(output))
        except FileNotFoundError:
            print("Error: Input file not found.")
        except Exception as e:
            print(f"Error reading file: {e}")


Homework().read_input()
