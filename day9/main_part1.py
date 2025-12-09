def read_red_tile_locations(file_path: str) -> list[tuple[int, int]]:
    tiles = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            x, y = line.strip().split(",")
            tiles.append((int(x), int(y)))
    return tiles


def main() -> None:
    FILE_PATH = "day9/input_small.txt"
    tiles = read_red_tile_locations(FILE_PATH)
    print(tiles)


if __name__ == "__main__":
    main()
