class Beam:
    """A class to analyze beam splits in a given pattern."""
    
    def __init__(self, input_file: str = "input/day_7.txt"):
        """Initialize the Beam analyzer.
        
        Args:
            input_file: Path to the input file
        """
        self.input_file = input_file
    
    def get_splits(self, data: list[str]) -> int:
        """Count the number of beam splits in the given data.
        
        Args:
            data: List of strings representing the pattern rows
            
        Returns:
            Number of beam splits found
        """
        if not data:
            return 0
        
        try:
            start_idx = data[0].index("S")
        except ValueError:
            return 0
        
        curr_idx_set = {start_idx}
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
    
    def read_input(self) -> list[str]:
        """Read input from file.
        
        Returns:
            List of strings from the input file
            
        Raises:
            FileNotFoundError: If input file doesn't exist
            IOError: If there's an error reading the file
        """
        try:
            with open(self.input_file, "r") as f:
                data = f.readlines()
            return [line.strip() for line in data if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {self.input_file}")
        except IOError as e:
            raise IOError(f"Error reading input file: {e}")
    
    def pipeline(self) -> int:
        """Run the complete analysis pipeline.
        
        Returns:
            Number of beam splits found
        """
        data = self.read_input()
        split_count = self.get_splits(data)
        return split_count


if __name__ == "__main__":
    try:
        beam = Beam()
        result = beam.pipeline()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)