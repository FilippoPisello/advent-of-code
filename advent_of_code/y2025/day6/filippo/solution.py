"""Solution for day 6 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    total = 0
    values: dict[int, list[int]] = {}
    for row in problem_input.splitlines():
        for index, value in enumerate(row.split()):
            if value.isdigit():
                if index not in values:
                    values[index] = []
                values[index].append(int(value))
            else:
                if value == "+":
                    total += sum(values[index])
                elif value == "*":
                    prod = 1
                    for v in values[index]:
                        prod *= v
                    total += prod
    return total


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
