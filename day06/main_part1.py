import math


def transpose(list_of_lists) -> list[list]:
    return list(map(tuple, zip(*list_of_lists)))


def read_homework_columns(file_path: str) -> list[tuple]:
    with open(file_path, "r") as f:
        lines = [line.strip().split() for line in f.readlines()]
    return transpose(lines)


def calculate_result(column: tuple) -> int:
    operand = column[-1]
    values = [int(v) for v in column[:-1]]
    if operand == "+":
        return sum(values)
    elif operand == "*":
        return math.prod(values)
    else:
        raise ValueError(f"Operand '{operand}' is not valid, something went wrong.")


def main():
    FILE_PATH = "day6/input.txt"
    columns = read_homework_columns(FILE_PATH)
    grand_total = 0
    for column in columns:
        grand_total += calculate_result(column)
    print(grand_total)


if __name__ == "__main__":
    main()
