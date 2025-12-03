class Lobby:
    def __init__(self):
        self.total_joltage = 0
        self.num_digits = 12

    def get_joltage(self, battery: str):
        joltage = [0 for _ in range(self.num_digits)]

        current_index = 0
        while current_index < self.num_digits:
            num_digits = self.num_digits - current_index
            digit_list = sorted(set(battery), reverse=True)
            for max_digit in digit_list:
                max_index = battery.index(max_digit)

                if len(battery) - max_index >= num_digits:
                    joltage[current_index] = max_digit
                    battery = battery[max_index + 1 :]
                    current_index += 1
                    break

        final_joltage = "".join(joltage)
        self.total_joltage += int(final_joltage)

    def read_input(self) -> list:
        with open("input/day_3.txt", "r") as f:
            batteries = f.readlines()

        return batteries

    def get_total_output(self):
        batteries = self.read_input()
        for battery in batteries:
            self.get_joltage(battery.strip())

        print(self.total_joltage)


Lobby().get_total_output()
