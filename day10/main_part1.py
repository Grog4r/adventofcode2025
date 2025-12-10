class Machine:

    def __init__(
        self,
        lights_goal: int,
        n_lights: int,
        button_masks: set[int],
        joltages: list[int],
    ) -> None:
        self.lights_goal = lights_goal
        self.n_lights = n_lights
        self.button_masks = button_masks
        self.joltages = joltages

    def construct_reasonable_button_seqs(self, button_seqs: list[tuple]) -> list[int]:
        next_button_seqs = []
        if len(button_seqs) == 0:
            return [(mask,) for mask in self.button_masks]
        
        for button_seq in button_seqs:
            unused_masks = self.button_masks.difference(set(button_seq))
            for mask in unused_masks:
                next_button_seqs.append(tuple([*button_seq, mask]))
        return next_button_seqs

    def try_reasonable_button_seqs(self) -> int:
        button_seqs = []
        found_solution = False
        while not found_solution:
            button_seqs = self.construct_reasonable_button_seqs(button_seqs)
            # print(button_seqs)
            for button_seq in button_seqs:
                if self.press_buttons_and_test(button_seq):
                    print(button_seq)
                    found_solution = True
                    return len(button_seq)
                    

    def press_buttons_and_test(self, button_seq: tuple[int], VERBOSE: bool = False) -> bool:
        result = 0
        for button in button_seq:
            if VERBOSE:
                print(f"b{result:b} XOR b{button:b}")
            result ^= button
        if VERBOSE:
            print(f"Result: b{result:b} ({result}) Searching: b{self.lights_goal:b} ({self.lights_goal})")
        return result == self.lights_goal


def button_to_mask(button: list[int]) -> int:
    button_mask = 0
    for connection in button:
        connection_mask = 1 << connection
        button_mask |= connection_mask
    return button_mask
    

def read_machines(file_path: str) -> list[Machine]:
    machines = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            lights_goal = line.split("]")[0].split("[")[1]
            lights_goal = lights_goal.replace(".", "0").replace("#", "1")[::-1]
            lights_goal_int = int(lights_goal, base=2)
            print(f"b{lights_goal} = {lights_goal_int}")

            buttons_str = line.split("]")[1].split("{")[0].strip()
            buttons_tuples = [
                tuple([int(v) for v in button.strip(") ").split(",")])
                for button in buttons_str.split("(")[1:]
            ]
            print(buttons_tuples)

            button_masks = set()
            for button in buttons_tuples:
                button_mask = button_to_mask(button)
                print(f"{button} -> b{button_mask:b} = {button_mask}")
                button_masks.add(button_mask)
            print(button_masks)

            joltages = [int(j) for j in line.split("{")[1].split("}")[0].split(",")]
            print(joltages)

            machine = Machine(lights_goal_int, len(lights_goal), button_masks, joltages)
            machines.append(machine)

    return machines


def main():
    FILE_PATH = "day10/input.txt"
    machines = read_machines(FILE_PATH)
    total_sum_pressed = 0
    for machine in machines:
        n_presses = machine.try_reasonable_button_seqs()
        print(n_presses)
        total_sum_pressed += n_presses
    print(f"Total number of buttons to press: {total_sum_pressed}")


if __name__ == "__main__":
    main()
