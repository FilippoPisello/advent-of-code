"""Solution for day 3 of Advent of Code 2024, by filippo."""

import re
from typing import Any

MUL_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"


def main_part_one(problem_input: str) -> Any:
    matches = re.finditer(MUL_PATTERN, problem_input)
    result = 0
    for match in matches:
        result += int(match[1]) * int(match[2])
    return result


def main_part_two(problem_input: str) -> Any:
    mul_matches = re.finditer(MUL_PATTERN, problem_input)

    do_pattern = "do()"
    dont_pattern = "don't()"
    do_indexes = [-1] + [m.start() for m in re.finditer(do_pattern, problem_input)]
    dont_indexes = [-2] + [m.start() for m in re.finditer(dont_pattern, problem_input)]

    result = 0
    for match in mul_matches:
        closest_do = max(i for i in do_indexes if i < match.start())
        closest_dont = max(i for i in dont_indexes if i < match.start())
        if closest_do > closest_dont:
            result += int(match[1]) * int(match[2])

    return result


# def main(problem_input: str) -> Any:
#    return
