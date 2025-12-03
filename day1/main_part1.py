file_path = "input.txt"


class Dial:
    MIN = 0
    MAX = 99

    number_of_0s = 0

    def __init__(self, starting_position: int) -> None:
        self.pos = starting_position

    def process_instruction(self, instruction: str) -> None:
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == "L":
            amount *= -1

        self.pos += amount
        self.pos = self.pos % (self.MAX + 1)

        if self.pos == 0:
            self.number_of_0s += 1

        print(f"{instruction} -> {self.pos}")



def main() -> None:
    dial = Dial(starting_position=50)

    with open(file_path) as f:
        for line in f.readlines():
            dial.process_instruction(line.strip())

    print(f"Number of 0s: {dial.number_of_0s}")
    


if __name__ == "__main__":
    main()
