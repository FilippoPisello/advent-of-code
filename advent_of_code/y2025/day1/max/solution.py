"""Solution for day 1 of Advent of Code 2025, by Max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    instructions = problem_input.splitlines()
    dial = 50
    ends_on_zero_count = 0

    for instruction in instructions:
        letter, number = instruction[0], int(instruction[1:])
        sign = 1 if letter == "R" else -1
        dial += sign * number
        dial = dial % 100

        ends_on_zero_count += 1 if dial == 0 else 0

    return ends_on_zero_count


def main_part_two(problem_input: str) -> Any:
    instructions = problem_input.splitlines()
    dial = 50
    pass_on_zero_count = 0

    for instruction in instructions:
        previous_dial = dial
        letter, number = instruction[0], int(instruction[1:])
        sign = 1 if letter == "R" else -1
        dial += sign * number

        rotations = max(abs(dial) // 100 + (dial <= 0) - (previous_dial == 0), 0)
        pass_on_zero_count += rotations
        dial = dial % 100
    return pass_on_zero_count
