import math


def transpose(list_of_lists) -> list[list]:
    return list(map(tuple, zip(*list_of_lists)))


def read_homework_columns(file_path: str) -> list[tuple]:
    with open(file_path, "r") as f:
        lines_raw = f.readlines()
        lines = [line.strip().split() for line in lines_raw]
        columns = transpose(lines)
        column_widths = []
        for column in columns:
            column_widths.append(max([len(v) for v in column]))
    lines_split_correctly = []
    for line in lines_raw:
        split_lines = []
        start_index = 0
        for column_width in column_widths:
            split_lines.append(line[start_index : start_index + column_width])
            start_index += column_width + 1
        lines_split_correctly.append(split_lines)
    return transpose(lines_split_correctly)


def convert_values(values: list[str]) -> list[int]:
    values_T = transpose([list(v) for v in values])
    ints = [int("".join(v).strip()) for v in values_T]
    return ints


def calculate_result(column: tuple) -> int:
    operand = column[-1].strip()
    values = convert_values(column[:-1])
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
