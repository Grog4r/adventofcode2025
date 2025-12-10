def read_ranges(file_path: str) -> list[tuple[int, int]]:
    with open(file_path, "r") as f:
        line = f.readline()
        ranges = [r for r in line.split(",")]
        return [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]


def find_invalid_ids(range_start: int, range_end: int) -> list[int]:
    invalid_ids = []
    for candidate in range(range_start, range_end + 1):
        candidate_str = str(candidate)
        candidate_split = len(candidate_str) // 2
        part_a = candidate_str[0:candidate_split]
        part_b = candidate_str[candidate_split:]
        if part_a == part_b:
            invalid_ids.append(candidate)
    return invalid_ids


def test_small_input():
    small_input_path = "day2/input_small.txt"
    ranges = read_ranges(small_input_path)

    all_invalid_ids = []
    for range_start, range_end in ranges:
        invalid_ids_for_range = find_invalid_ids(range_start, range_end)
        print(f"[{range_start}, {range_end}]:\n{invalid_ids_for_range}")
        all_invalid_ids += invalid_ids_for_range

    assert sum(all_invalid_ids) == 1227775554


def main():
    input_path = "day2/input.txt"
    ranges = read_ranges(input_path)

    all_invalid_ids = []
    for range_start, range_end in ranges:
        invalid_ids_for_range = find_invalid_ids(range_start, range_end)
        print(f"[{range_start}, {range_end}]:\n{invalid_ids_for_range}")
        all_invalid_ids += invalid_ids_for_range

    print(sum(all_invalid_ids))


if __name__ == "__main__":
    test_small_input()
    main()
