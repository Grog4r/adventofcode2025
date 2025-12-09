from shapely.geometry import Point, box
from shapely.geometry.polygon import Polygon


def read_corners(file_path: str) -> list[Point]:
    points = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            x, y = line.strip().split(",")
            points.append(Point(int(x), int(y)))
    return points


def calculate_tile_surface(corner_a: Point, corner_b: Point) -> int:
    x_len = abs(corner_a.x - corner_b.x) + 1
    y_len = abs(corner_a.y - corner_b.y) + 1
    return x_len * y_len


def corners_to_rect(corner_a: Point, corner_b: Point) -> tuple[Point, Point]:
    x_a = corner_a.x
    y_a = corner_a.y
    x_b = corner_b.x
    y_b = corner_b.y
    return box(min(x_a, x_b), min(y_a, y_b), max(x_a, x_b), max(y_a, y_b))


def main() -> None:
    FILE_PATH = "day9/input.txt"
    corners = read_corners(FILE_PATH)
    polygon = Polygon(corners)
    max_surface = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            corner_a = corners[i]
            corner_b = corners[j]
            rect = corners_to_rect(corner_a, corner_b)
            if polygon.covers(rect):
                surface = calculate_tile_surface(corner_a, corner_b)
                max_surface = max(max_surface, surface)

    print(int(max_surface))


if __name__ == "__main__":
    main()
    print()
