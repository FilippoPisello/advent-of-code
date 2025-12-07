"""Solution for day 6 of Advent of Code 2025, by david."""

from itertools import zip_longest
from typing import Any
import operator

ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}


def main_part_one(problem_input: str) -> Any:
    problems = format_input(problem_input)
    transposed = [list(col) for col in zip(*problems)]
    total = 0
    for column in transposed:
        if column[len(column) - 1] == "+":
            total += sum(map(int, column[:-1]))
        elif column[len(column) - 1] == "*":
            total += prod(column[:-1])
            continue

    return total


# 6019576291014
def main_part_two(problem_input: str) -> Any:

    grand_total = 0
    lines = problem_input.splitlines()

    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]

    rows = len(grid)
    cols = max_len

    grand_total = 0
    current_problem_nums = []
    current_operator = None

    for c in range(cols - 1, -1, -1):
        col_chars = [grid[r][c] for r in range(rows)]

        digit_chars = col_chars[:-1]
        operator_char = col_chars[-1]

        is_separator = all(char == " " for char in digit_chars)

        if is_separator:
            if current_problem_nums:
                grand_total += calculate_problem(current_problem_nums, current_operator)
                current_problem_nums = []
                current_operator = None
            continue

        digit_str = "".join(digit_chars).replace(" ", "")

        if digit_str:
            number = int(digit_str)
            current_problem_nums.append(number)

        if operator_char in ("+", "*"):
            current_operator = operator_char

    if current_problem_nums:
        grand_total += calculate_problem(current_problem_nums, current_operator)

    return grand_total


def calculate_problem(numbers, operator):
    if not numbers:
        return 0

    if operator is None:
        return sum(numbers)

    result = numbers[0]
    for num in numbers[1:]:
        if operator == "+":
            result += num
        elif operator == "*":
            result *= num

    return result


def format_input(input: str) -> Any:
    input_lines = input.splitlines()
    grid = [row.split() for row in input_lines]
    return grid


def prod(list: list[str]) -> int:
    result = 1
    for n in list:
        result *= int(n)
    return result


# def main(problem_input: str) -> Any:
#    return
