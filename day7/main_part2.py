class TachyonMap:

    START = "S"
    EMPTY = "."
    BEAM = "|"
    SPLITTER = "^"

    tile_map = []
    tile_map_simulated = []
    used_splitter = 0

    def __init__(self, file_path: str) -> None:
        self._read_input(file_path)

    def _read_input(self, file_path: str) -> None:
        with open(file_path, "r") as f:
            for line in f.readlines():
                self.tile_map.append(list(line.strip()))

    def print_input_map(self) -> None:
        output_str = ""
        for line in self.tile_map:
            output_str += "".join(line) + "\n"
        print(output_str)
    
    def print_simulated_map(self) -> None:
        output_str = ""
        for line in self.tile_map_simulated:
            output_str += "".join(line) + "\n"
        print(output_str)

    def _propagate_beams_in_line(
        self, line: list[str], beam_indices: dict[int]
    ) -> list[str]:
        current_line = line.copy()
        for i, symbol in enumerate(line):

            if symbol == self.START:
                beam_indices[i] = 1
                continue

            elif symbol == self.SPLITTER:
                if i in beam_indices:
                    self.used_splitter += 1
                    n_beams = beam_indices[i]
                    del beam_indices[i]
                    prev = i - 1
                    next = i + 1
                    if prev >= 0:
                        beam_indices[prev] = beam_indices.get(prev, 0) + n_beams
                        current_line[prev] = self.BEAM
                    if next < len(current_line):
                        beam_indices[next] = beam_indices.get(next, 0) + n_beams
                        current_line[next] = self.BEAM
                continue
            
            if i in beam_indices:
                current_line[i] = self.BEAM

        return current_line, beam_indices

    def simulate_beams(self, VERBOSE: bool = False) -> None:
        beam_indices = {}
        for line in self.tile_map:
            current_line, beam_indices = self._propagate_beams_in_line(
                line, beam_indices
            )
            self.tile_map_simulated.append(current_line)
            if VERBOSE:
                print("".join(line))
                print("--->")
                print("".join(current_line))
                print(beam_indices)
                print()
        print(self.used_splitter)
        print(sum(beam_indices.values()))


def main():
    FILE_PATH = "day7/input.txt"
    tachyon_map = TachyonMap(FILE_PATH)
    tachyon_map.print_input_map()
    tachyon_map.simulate_beams(True)
    # tachyon_map.print_simulated_map()


if __name__ == "__main__":
    main()
