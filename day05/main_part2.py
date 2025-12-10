def process_input(file_path: str) -> list[tuple[int, int]]:
    ranges = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                break

            split_line = line.split("-")
            start = int(split_line[0])
            end = int(split_line[1])
            ranges.append((start, end))

    return ranges


def combine_ranges(range_l: tuple, range_r: tuple):
    # Same range
    if range_l == range_r:
        return [range_l]

    # Same start
    if range_l[0] == range_r[0]:
        return [range_r]

    # Same end
    if range_l[1] == range_r[1]:
        return [range_l]

    # Combine ranges
    if range_l[1] >= range_r[0]:
        if range_l[1] >= range_r[1]:
            return [range_l]
        return [(range_l[0], range_r[1])]


    
    return [range_l, range_r]


def sanitize_id_ranges(ranges):
    new_ranges = []
    ranges = sorted(ranges)
    current_index = 0
    merge_done = False

    while current_index < len(ranges) - 1:
        range_l = ranges[current_index]
        range_r = ranges[current_index + 1]
        new_range = combine_ranges(range_l, range_r)
        print(f"{range_l} + {range_r} -> {new_range}")
        new_ranges += [new_range[0]]
        merge_done = merge_done or len(new_range) == 1
        current_index += 1
        if merge_done:
            new_ranges += ranges[current_index + 1 :]
            ranges = sorted(new_ranges)
            print(ranges)
            current_index = 0
            new_ranges = []
            merge_done = False

    return ranges


def number_of_fresh_in_range(start: int, end: int) -> int:
    return end - start + 1


def test_combine_ranges():
    assert combine_ranges((1, 1), (1, 1)) == [(1, 1)]

    assert combine_ranges((1, 8), (1, 8)) == [(1, 8)]

    assert combine_ranges((1, 6), (1, 8)) == [(1, 8)]

    assert combine_ranges((1, 8), (3, 8)) == [(1, 8)]

    assert combine_ranges((1, 5), (3, 8)) == [(1, 8)]

    assert combine_ranges((1, 8), (3, 5)) == [(1, 8)]

    assert combine_ranges((1, 4), (5, 8)) == [(1, 4), (5, 8)]


def main() -> None:
    FILE_PATH = "day5/input.txt"
    ranges = process_input(FILE_PATH)
    ranges = sanitize_id_ranges(ranges)
    print(ranges)

    total_range_of_fresh = 0
    for start, end in ranges:
        total_range_of_fresh += number_of_fresh_in_range(start, end)

    print(total_range_of_fresh)


if __name__ == "__main__":
    test_combine_ranges()
    main()
