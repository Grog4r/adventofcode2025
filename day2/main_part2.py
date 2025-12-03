def read_ranges(file_path: str) -> list[tuple[int, int]]:
    with open(file_path, "r") as f:
        line = f.readline()
        ranges = [r for r in line.split(",")]
        return [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]


def split_candidate_is_symmetrical(candidate: str, split_length: int) -> bool:
    splitpoint_l = 0
    splitpoint_r = split_length
    comparable = candidate[splitpoint_l:splitpoint_r]
    while splitpoint_r <= len(candidate):
        next_comparable = candidate[splitpoint_l:splitpoint_r]
        if comparable != next_comparable:
            return False
        comparable = next_comparable
        splitpoint_l = splitpoint_r
        splitpoint_r += split_length
        
    return True


def find_invalid_ids(range_start: int, range_end: int) -> list[int]:
    invalid_ids = set()
    for candidate in range(range_start, range_end + 1):
        candidate_str = str(candidate)
        candidate_len = len(candidate_str)
        split_lengths = list(range(1, candidate_len // 2 + 1))
        for split_candidate in split_lengths:
            if candidate_len / split_candidate != candidate_len // split_candidate:
                # print(f"Skipping split_candidate {split_candidate}")
                continue
            if split_candidate_is_symmetrical(candidate_str, split_candidate):
                invalid_ids.add(candidate)
                break
    return invalid_ids


def test_small_input():
    small_input_path = "day2/input_small.txt"
    ranges = read_ranges(small_input_path)

    all_invalid_ids = []
    for range_start, range_end in ranges:
        invalid_ids_for_range = find_invalid_ids(range_start, range_end)
        print(f"[{range_start}, {range_end}]:\n{invalid_ids_for_range}")
        all_invalid_ids += invalid_ids_for_range

    assert sum(all_invalid_ids) == 4174379265


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
