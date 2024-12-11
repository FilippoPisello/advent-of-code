"""Solution for day 11 of Advent of Code 2024, by david."""

from typing import Any
import re
import math


def main_part_one(problem_input: str) -> Any:
    rocks = problem_input.split(" ")
    rocks_int = {int(x): 1 for x in rocks}

    for _ in range(25):
        rocks_int = step_int_dict(rocks_int)

    total = 0
    for x in rocks_int.values():
        total += x

    return total


def main_part_two(problem_input: str) -> Any:
    rocks = problem_input.split(" ")
    rocks_int = {int(x): 1 for x in rocks}

    for _ in range(75):
        rocks_int = step_int_dict(rocks_int)

    total = 0
    for x in rocks_int.values():
        total += x

    return total


def step_int_dict(rocks_int):
    new_rocks_int = {}
    for mark, stones in rocks_int.items():
        if mark == 0:
            if 1 in new_rocks_int.keys():
                new_rocks_int[1] += stones
            else:
                new_rocks_int[1] = stones
            continue
        l = math.floor(math.log10(mark)) + 1
        if l % 2 == 0:
            a = mark // 10 ** (l // 2)
            b = mark % 10 ** (l // 2)
            if a in new_rocks_int.keys():
                new_rocks_int[a] += stones
            else:
                new_rocks_int[a] = stones

            if b in new_rocks_int.keys():
                new_rocks_int[b] += stones
            else:
                new_rocks_int[b] = stones
        else:
            if mark * 2024 in new_rocks_int.keys():
                new_rocks_int[mark * 2024] += stones
            else:
                new_rocks_int[mark * 2024] = stones

    return new_rocks_int


# def main(problem_input: str) -> Any:
#    return
