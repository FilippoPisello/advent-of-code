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
    position = 50
    pass_on_zero = 0
    for line in problem_input.splitlines():
        direction, ticks_moved = line[0], int(line[1:])
        sign = 1 if direction == "R" else -1
        new_unconstrained_position = position + sign * ticks_moved
        new_position = new_unconstrained_position % 100

        if sign == 1:
            pass_on_zero += new_unconstrained_position // 100
        else:
            pass_on_zero += (
                # If we hit or crossed zero, count
                (new_unconstrained_position <= 0)
                # Count how many hundreds we crossed
                + (abs(new_unconstrained_position) // 100)
                # If we started at zero, we already counted it, so subtract one
                - (position == 0)
            )

        position = new_position
    return pass_on_zero


# def main(problem_input: str) -> Any:
#    return
