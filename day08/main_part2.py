from copy import deepcopy
import numpy as np


class JunctionBox:

    def __init__(self, id: int, position: tuple[int, int, int]) -> None:
        self.id = id
        self.position = np.array(position)

    def __repr__(self) -> str:
        return f"[{self.id}]: {self.position}"


def read_circuits(file_path: str) -> list[JunctionBox]:
    circuits = []
    with open(file_path, "r") as f:
        for i, line in enumerate(f.readlines()):
            position = tuple([int(c) for c in line.strip().split(",")])
            circuits.append(JunctionBox(i, position))
    return circuits


def distance(box_a: JunctionBox, box_b: JunctionBox) -> float:
    return np.linalg.norm(box_a.position - box_b.position)


def position_of_lowest_distance(distance_matrix: np.ndarray) -> tuple[int, int]:
    return (
        int(v)
        for v in np.unravel_index(
            np.argmin(distance_matrix, axis=None), distance_matrix.shape
        )
    )


def merge_circuits(id_a: int, id_b: int, circuits: list[list[int]]) -> list[list[int]]:
    new_circuits = deepcopy(circuits)
    circuit_a = circuit_b = None
    for c in circuits:
        if id_a in c:
            circuit_a = c
            new_circuits.remove(c)
        elif id_b in c:
            circuit_b = c
            new_circuits.remove(c)

    # Case that a and b are already in a circuit
    if circuit_b is None:
        new_circuit = circuit_a
    else:
        new_circuit = circuit_a + circuit_b

    new_circuits.append(new_circuit)
    return new_circuits


def main() -> None:
    TEST_RUN = False
    if TEST_RUN:
        FILE_PATH = "day8/input_small.txt"
    else:
        FILE_PATH = "day8/input.txt"

    junction_boxes = read_circuits(FILE_PATH)
    if TEST_RUN:
        print(junction_boxes)
    distance_matrix = np.full((len(junction_boxes), len(junction_boxes)), np.inf)
    for i in range(len(junction_boxes)):
        j_start = i + 1
        for j in range(j_start, len(junction_boxes)):
            if i == j:
                continue
            box_a = junction_boxes[i]
            box_b = junction_boxes[j]
            dist = distance(box_a, box_b)
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist

    circuits = [[j.id] for j in junction_boxes]
    last_a_x = None
    last_b_x = None
    while len(circuits) > 1:
        i, j = position_of_lowest_distance(distance_matrix)
        last_a_x = junction_boxes[i].position[0]
        last_b_x = junction_boxes[j].position[0]
        if TEST_RUN:
            print(
                f"Merging boxes {i} ({junction_boxes[i].position}) and {j} ({junction_boxes[j].position})..."
            )
        distance_matrix[i, j] = np.inf
        distance_matrix[j, i] = np.inf
        circuits = merge_circuits(i, j, circuits)
        if TEST_RUN:
            print(circuits)

    print(last_a_x * last_b_x)


if __name__ == "__main__":
    main()
