class Lobby:
    def __init__(self):
        self.total_joltage = 0

    def get_joltage(self, battery: str):
        digit_1 = max(battery)
        index_1 = battery.index(digit_1)

        if index_1 == (len(battery) - 1):
            digit_2 = digit_1
            battery = battery[:index_1]
            digit_1 = max(battery)

        else:
            battery = battery[index_1 + 1 :]
            digit_2 = max(battery)

        joltage = int(digit_1 + digit_2)
        self.total_joltage += joltage

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
