class Beam:
    def get_splits(self, data: list):
        """
        Calculate the number of splits in the beam data.
        
        Args:
            data: List of strings representing the beam data.
        
        Returns:
            Count of splits.
        """
        try:
            start_idx = data[0].index("S")
            curr_idx_set = set([start_idx])
            next_idx_set = set()
            split_count = 0

            for row in data[1:]:
                if "^" in row:
                    for idx in curr_idx_set:
                        if row[idx] == "^":
                            split_count += 1
                            if idx - 1 >= 0:
                                next_idx_set.add(idx - 1)
                            if idx + 1 < len(row.strip()):
                                next_idx_set.add(idx + 1)
                        else:
                            next_idx_set.add(idx)
                    curr_idx_set = next_idx_set
                    next_idx_set = set()

            return split_count
        except Exception as e:
            print(f"Error calculating splits: {e}")
            return 0

    def read_input(self) -> list:
        """
        Read input from the file.
        
        Returns:
            List of strings representing the beam data.
        """
        try:
            with open("input/day_7.txt", "r") as f:
                data = f.readlines()

            return data
        except FileNotFoundError:
            print("Error: Input file not found.")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def pipeline(self):
        """Execute the pipeline operation."""
        data = self.read_input()
        split_count = self.get_splits(data)

        print(split_count)


Beam().pipeline()
