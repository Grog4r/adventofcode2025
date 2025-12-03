file_path = "day1/input.txt"


class Dial:

    number_of_0s_total = 0

    def __init__(self, starting_position: int) -> None:
        self.pos = starting_position
        print(f"The dial starts by pointing at {starting_position}.")

    def process_instruction(self, instruction: str) -> None:
        direction = instruction[0]
        amount = int(instruction[1:])

        print(f"Instruction: {instruction}. Position currently: {self.pos}")

        if direction == "L":
            while amount > 0:
                if self.pos == 0:
                    self.pos = 99
                    amount -= 1
                if amount >= self.pos:
                    amount -= self.pos
                    print(f"Turned {self.pos} to the left, passing 0.")
                    self.pos = 0
                    self.number_of_0s_total += 1
                else:
                    self.pos -= amount
                    print(f"Turned {amount} to the left, landing on {self.pos}.")
                    amount = 0

        else:
            while amount > 0:
                if amount >= (100 - self.pos):
                    amount -= (100 - self.pos)
                    print(f"Turned {100 - self.pos} to the right, passing 0.")
                    self.pos = 0
                    self.number_of_0s_total += 1
                else:
                    self.pos += amount
                    print(f"Turned {amount} to the right, landing on {self.pos}.")
                    amount = 0



def main() -> None:
    dial = Dial(starting_position=50)

    with open(file_path) as f:
        for line in f.readlines():
            dial.process_instruction(line.strip())

    print(f"Number of 0s: {dial.number_of_0s_total}")


def test_a():
    dial = Dial(0)
    for line, expected_pos, expected_0s_total in [("L100", 0, 1), ("R100", 0, 2), ("R10", 10, 2), ("L110", 0, 4)]:
        dial.process_instruction(line)
        assert dial.pos == expected_pos
        assert dial.number_of_0s_total == expected_0s_total

if __name__ == "__main__":
    test_a()
    main()
