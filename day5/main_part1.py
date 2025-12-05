def process_input(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ids = []

    is_ranges = True
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                is_ranges = False
                continue

            if is_ranges:
                split_line = line.split("-")
                start = int(split_line[0])
                end = int(split_line[1])
                ranges.append((start, end))

            else:
                ids.append(int(line))

    return ranges, ids


def check_id_in_ranges(id, ranges) -> bool:
    for start, end in ranges:
        if id >= start and id <= end:
            return True
    return False


def main() -> None:
    FILE_PATH = "day5/input.txt"
    ranges, ids = process_input(FILE_PATH)
    print(ranges)
    print(ids)
    number_of_fresh = 0
    for id in ids:
        number_of_fresh += int(check_id_in_ranges(id, ranges))

    print(number_of_fresh)


if __name__ == "__main__":
    main()
