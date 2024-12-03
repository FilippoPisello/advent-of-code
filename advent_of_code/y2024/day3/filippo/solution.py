"""Solution for day 3 of Advent of Code 2024, by filippo."""

import re
from typing import Any


def main_part_one(problem_input: str) -> Any:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(problem_input)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
