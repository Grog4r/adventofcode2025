def read_batteries(file_path: str) -> list[int]:
    with open(file_path, "r") as f:
        return [int(v) for v in f.readlines()]

def find_joltage(battery: int) -> int:
    digits = [int(digit) for digit in str(battery)]
    first = max(digits[:-1])
    first_index = digits.index(first)
    second = max(digits[first_index+1:])
    joltage = int(f"{first}{second}")
    print(f"{battery} -> {joltage}")
    return joltage

def main() -> None:
    FILE_PATH = "day3/input.txt"
    batteries = read_batteries(FILE_PATH)
    joltages = [find_joltage(b) for b in batteries]
    print(sum(joltages))


if __name__ == "__main__":
    main()