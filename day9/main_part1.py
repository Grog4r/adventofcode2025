def read_red_tile_locations(file_path: str) -> list[tuple[int, int]]:
    tiles = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            x, y = line.strip().split(",")
            tiles.append((int(x), int(y)))
    return tiles

def calculate_tile_surface(tile_a: tuple[int, int], tile_b: tuple[int, int]) -> int:
    x_len = abs(tile_a[0] - tile_b[0]) + 1
    y_len = abs(tile_a[1] - tile_b[1]) + 1
    return x_len * y_len

def main() -> None:
    FILE_PATH = "day9/input.txt"
    tiles = read_red_tile_locations(FILE_PATH)
    print(tiles)
    max_surface = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            assert j > i
            tile_a = tiles[i]
            tile_b = tiles[j]
            surface = calculate_tile_surface(tile_a, tile_b)
            print(f"{tile_a} - {tile_b}: {surface} tile²")
            max_surface = max(max_surface, surface)
    print(max_surface)



if __name__ == "__main__":
    main()
