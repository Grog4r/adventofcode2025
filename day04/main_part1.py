class PaperMap:

    paper_map = []

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.paper_map.append(list(line.strip()))

    def print_map(self) -> None:
        paper_map = ""
        for y in range(len(self.paper_map)):
            for x in range(len(self.paper_map[0])):
                paper_map += self.paper_map[y][x]
            paper_map += "\n"
        print(paper_map)

    def surroundings_less_than_4(self, x, y) -> bool:
        free = 0
        for y_delta in [-1, 0, 1]:
            for x_delta in [-1, 0, 1]:
                x_check = x + x_delta
                y_check = y + y_delta
                if (x_check < 0 or x_check >= len(self.paper_map[y])) or (
                    y_check < 0 or y_check >= len(self.paper_map)
                ):
                    free += 1
                else:
                    if self.paper_map[y_check][x_check] == ".":
                        free += 1
        return free > 4

    def print_checked_paper_map(self) -> None:
        checked_paper_map = ""
        for y in range(len(self.paper_map)):
            for x in range(len(self.paper_map[0])):
                if self.paper_map[y][x] == ".":
                    checked_paper_map += "."
                else:
                    checked_paper_map += (
                        "x" if self.surroundings_less_than_4(x, y) else "@"
                    )
            checked_paper_map += "\n"
        print(checked_paper_map)

    def count_free_paper_rolls(self) -> int:
        free_paper_rolls = 0
        for y in range(len(self.paper_map)):
            for x in range(len(self.paper_map[0])):
                if self.paper_map[y][x] == "@":
                    free_paper_rolls += int(self.surroundings_less_than_4(x, y))
        return free_paper_rolls


def read_map(file_path: str) -> PaperMap:
    lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        return PaperMap(lines)


def main() -> None:
    FILE_PATH = "day4/input.txt"
    paper_map = read_map(FILE_PATH)
    paper_map.print_map()
    paper_map.print_checked_paper_map()
    free_paper_rolls = paper_map.count_free_paper_rolls()
    print(free_paper_rolls)


if __name__ == "__main__":
    main()
