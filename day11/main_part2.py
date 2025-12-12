class Device:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inputs: list[str] = []
        self.n_ways_to_out = 0

    def connect_to_input(self, input: str) -> None:
        self.inputs.append(input)

    def __repr__(self) -> str:
        return_str = f"[{self.name}]\n"
        return_str += "".join([f"  <-- [{c}]\n" for c in self.inputs])
        return_str += "\n"
        return return_str


def read_connections(file_path: str) -> dict[str, Device]:
    devices: dict[str, Device] = {"out": Device("out")}
    connections = {}
    with open(file_path, "r") as f:

        for line in f.readlines():
            input = line.split(":")[0]
            device = Device(input)
            devices[input] = device
            outputs = line.split(":")[1].strip().split()
            for output in outputs:
                connections[output]: list = connections.get(output, list())
                connections[output].append(input)

        print(connections)

        for output, inputs in connections.items():
            for input in inputs:
                devices[output].connect_to_input(input)

                print(f"{input} --> {output}")

    return devices


def add_to_state(state: tuple[int, int], summand: tuple[int, int]) -> tuple[int, int]:
    return (
        state[0] + summand[0],
        state[1] + summand[1],
        state[2] + summand[2],
        state[3] + summand[3],
    )


def recursively_go_back(
    devices: dict[str, Device],
    device_name: str,
    known_results: dict[str, tuple[int, int]],
) -> tuple[int, int]:
    if device_name in known_results:
        # print(f"I already know what the result of {device_name} is :)")
        return known_results[device_name]

    if device_name == "svr":
        state = (1, 0, 0, 0)
        known_results[device_name] = state
        return state

    state = (0, 0, 0, 0)

    device = devices[device_name]
    for input_name in device.inputs:
        input_state = recursively_go_back(devices, input_name, known_results)
        state = add_to_state(state, input_state)

    if device_name == "dac":
        state = (0, state[0], 0, state[2])
    elif device_name == "fft":
        state = (0, 0, state[0], state[1])

    # print(f"Adding a known result for {device_name} :)")
    known_results[device_name] = state
    # print(known_results)
    return state


def start_recursion(devices: dict[str, Device]) -> int:
    cache = {}
    final_state = recursively_go_back(devices, "out", cache)
    print(final_state)
    return min(final_state)


def main():
    FILE_PATH = "day11/input_small_part2.txt"
    FILE_PATH = "day11/input.txt"
    devices = read_connections(FILE_PATH)
    # for device in devices.values():
    #     print(device)

    n_outs = start_recursion(devices)
    print(f"Number of paths to out over dac and fft: {n_outs}.")


if __name__ == "__main__":
    main()
