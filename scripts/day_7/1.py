class Beam:
    def get_splits(self, data: list):
        """
        Calculate the number of beam splits in the given data.
        
        Args:
            data: List of strings representing the input grid.
            
        Returns:
            int: Number of beam splits encountered.
        """
        if not data or len(data) == 0:
            return 0
            
        start_idx = data[0].index("S")
        curr_idx_set = set([start_idx])
        next_idx_set = set()
        beam_split_count = 0

        for row in data[1:]:
            next_idx_set = set()  # Reset for each row
            if "^" in row:
                for idx in curr_idx_set:
                    if row[idx] == "^":
                        beam_split_count += 1
                        if idx - 1 >= 0:
                            next_idx_set.add(idx - 1)
                        if idx + 1 < len(row.rstrip()):
                            next_idx_set.add(idx + 1)
                    else:
                        next_idx_set.add(idx)
                curr_idx_set = next_idx_set

        return beam_split_count

    def read_input(self) -> list:
        """
        Read input data from the file.
        
        Returns:
            list: List of strings representing the input grid.
        """
        try:
            with open("input/day_7.txt", "r") as f:
                data = f.readlines()
            return data
        except FileNotFoundError:
            print("Error: Input file not found.")
            return []

    def pipeline(self):
        """
        Main pipeline to execute the beam split calculation.
        """
        data = self.read_input()
        if not data:
            print("No data to process.")
            return
            
        beam_split_count = self.get_splits(data)
        print(beam_split_count)


Beam().pipeline()