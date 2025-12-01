"""Solution for day 1 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    position = 50
    pass_on_zero = 0
    for line in problem_input.splitlines():
        letter, number = line[0], int(line[1:])
        sign = 1 if letter == "R" else -1
        new_unconstrained_position = position + sign * number
        position = new_unconstrained_position % 100
        pass_on_zero += position == 0
    return pass_on_zero


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
