class Device:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections = []

    def connect(self, other) -> None:
        self.connections.append(other)

    def __repr__(self) -> str:
        return_str = f"[{self.name}]\n"
        return_str += "".join([f'  --> [{c.name}]\n' for c in self.connections])
        return_str += "\n"
        return return_str


def read_connections(file_path: str) -> dict[str, Device]:
    devices: dict[str, Device] = {"out": Device("out")}
    connections = {}
    with open(file_path, "r") as f:

        for line in f.readlines():
            name = line.split(":")[0]
            device = Device(name)
            devices[name] = device
            connections[name] = line.split(":")[1].strip().split()

        for name, dev_conns in connections.items():
            for connection in dev_conns:
                other = devices[connection]
                devices[name].connect(other)

                print(f"Connecting {name} to {connection}")

    return devices


def start_iterating(devices: dict[str, Device]) -> int:
    n_outs = 0
    current_devices = ["you"]
    # print(current_devices)

    while not all([dev == "out" for dev in current_devices]):
        new_current_devices = []
        for dev_name in current_devices:
            dev = devices[dev_name]
            new_current_devices += [d.name for d in dev.connections]
        current_devices = new_current_devices
        n_outs += len([dev for dev in current_devices if dev == "out"])
        # print(current_devices)
    
    return n_outs
    

def main():
    FILE_PATH = "day11/input.txt"
    devices = read_connections(FILE_PATH)
    for device in devices.values():
        print(device)

    n_outs = start_iterating(devices)
    print(f"Number of paths to out: {n_outs}.")


if __name__ == "__main__":
    main()
