def read_batteries(file_path: str) -> list[int]:
    with open(file_path, "r") as f:
        return [int(v) for v in f.readlines()]


def find_joltage(battery: int, n_batteries: int) -> int:
    digits = [int(digit) for digit in str(battery)]
    n_digits = len(digits)
    joltage_list = []
    current_split_index = 0
    for i in range(n_batteries, 0, -1):
        if i-1 > 0:
            current_search = digits[: -(i-1)]
        else:
            current_search = digits

        current = max(current_search)
        joltage_list.append(current)
        current_split_index = digits.index(current)
        digits = digits[current_split_index + 1:]

    joltage = int("".join([str(j) for j in joltage_list]))
    print(f"{battery} -> {joltage}")
    return joltage


def main() -> None:
    FILE_PATH = "day3/input.txt"
    batteries = read_batteries(FILE_PATH)
    joltages = [find_joltage(b, 12) for b in batteries]
    print(sum(joltages))


if __name__ == "__main__":
    main()
