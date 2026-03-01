class Ingredients:
    def __init__(self):
        self.fresh_count = 0
        self.fresh_range = {}

    def is_fresh(self, id: int):
        """
        Check if an ID is within any of the fresh ranges.
        
        Args:
            id: ID to check.
        """
        try:
            for left, right in self.fresh_range.items():
                if id >= left:
                    if id <= right:
                        self.fresh_count += 1
                        break
        except Exception as e:
            print(f"Error checking freshness: {e}")

    def read_input(self) -> list:
        """
        Read input from the file.
        
        Returns:
            List of IDs to check.
        """
        try:
            with open("input/day_5.txt", "r") as f:
                data = f.readlines()

            ids = []
            flag = True
            for row in data:
                if row == "\n":
                    flag = False
                    continue
                if flag:
                    try:
                        left, right = map(int, row.strip().split("-"))
                        if left in self.fresh_range.keys():
                            self.fresh_range[left] = max(right, self.fresh_range[left])
                        else:
                            self.fresh_range[left] = right
                    except Exception as e:
                        print(f"Error parsing range: {e}")
                        continue
                else:
                    try:
                        ids.append(int(row.strip()))
                    except Exception as e:
                        print(f"Error parsing ID: {e}")
                        continue

            return ids
        except FileNotFoundError:
            print("Error: Input file not found.")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def get_fresh_count(self):
        """Calculate the total count of fresh IDs."""
        ids = self.read_input()
        for id in ids:
            self.is_fresh(id)

        print(self.fresh_count)


Ingredients().get_fresh_count()
