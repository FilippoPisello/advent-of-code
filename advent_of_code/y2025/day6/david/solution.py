"""Solution for day 6 of Advent of Code 2025, by david."""

from itertools import zip_longest
from typing import Any


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


def main_part_two(problem_input: str) -> Any:
    problems = format_input(problem_input)
    transposed = [list(col) for col in zip(*problems)]
    total = 0
    for column in transposed:
        cephalopod_column = format_column_cephalopod(column[:-1])
        print(cephalopod_column)
    return total


def format_input(input: str) -> Any:
    input_lines = input.splitlines()
    grid = [row.split() for row in input_lines]
    return grid


def prod(list: list[str]) -> int:
    result = 1
    for n in list:
        result *= int(n)
    return result


def format_column_cephalopod(column: list[str]) -> list[str]:

    print(column)
    reversed_parts = [p[::-1] for p in column]
    print(reversed_parts)
    columns = list(zip_longest(*reversed_parts, fillvalue=""))
    print(columns)
    outputs = ["".join(col) for col in columns]
    return outputs


# def main(problem_input: str) -> Any:
#    return
