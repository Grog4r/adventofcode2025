import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

class Machine:

    def __init__(
        self,
        buttons: list[tuple],
        joltage: tuple,
    ) -> None:
        self.buttons = buttons
        print(buttons)
        self.goal_joltage = joltage

    def find_minimum_button_presses(self) -> int:
        a = np.array(self.buttons).T

        c = np.ones(len(self.buttons))

        constraints = LinearConstraint(A=a, lb=self.goal_joltage, ub=self.goal_joltage)

        integrality = np.ones(len(self.buttons))

        bounds = Bounds(lb=0, ub=np.inf)

        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

        if res.success:
            solution_floats = res.x
            solution_integers = np.round(solution_floats).astype(int)
            
            return np.sum(solution_integers)
        else:
            raise RuntimeError(f"Some error occured while solving {a}\n===\n{self.goal_joltage}")


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
            buttons_str = line.split("]")[1].split("{")[0].strip()
            buttons_tuples = [
                tuple([int(v) for v in button.strip(") ").split(",")])
                for button in buttons_str.split("(")[1:]
            ]

            joltages = tuple(
                [int(j) for j in line.split("{")[1].split("}")[0].split(",")]
            )
            print(joltages)

            buttons = []
            for button in buttons_tuples:
                button_mask = button_to_mask(button)
                print(f"{button} -> b{button_mask:b}")
                buttons.append(
                    tuple([int(v) for v in f"{button_mask:0>{len(joltages)}b}"[::-1]])
                )

            machine = Machine(buttons, joltages)
            machines.append(machine)

    return machines


def main():
    FILE_PATH = "day10/input.txt"
    machines = read_machines(FILE_PATH)
    total_sum_pressed = 0
    for machine in machines:
        n_presses = machine.find_minimum_button_presses()
        print(n_presses)
        total_sum_pressed += n_presses
    print(f"Total number of buttons to press: {total_sum_pressed}")


if __name__ == "__main__":
    main()
