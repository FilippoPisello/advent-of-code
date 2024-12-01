"""Solution for day 1 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    left_list, right_list = [], []
    for line in problem_input.splitlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    return sum(
        abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list))
    )


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
