"""Solution for day 3 of Advent of Code 2024, by filippo."""

import re
from typing import Any

MUL_PATTERN = r"mul\((\d+),(\d+)\)"


def main_part_one(problem_input: str) -> Any:
    reg = re.compile(MUL_PATTERN)
    matches = reg.findall(problem_input)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result


def main_part_two(problem_input: str) -> Any:
    reg = re.compile(".*" + MUL_PATTERN)
    do_pattern = "do()"
    dont_pattern = "don't()"

    do = True
    result = 0
    start_index = 0
    for current_index, _ in enumerate(problem_input, start=1):
        substr = problem_input[start_index:current_index]
        if do_pattern in substr:
            do = True
            start_index = current_index
        elif dont_pattern in substr:
            do = False
            start_index = current_index
        elif (mul := reg.match(substr)) and do:
            result += int(mul[1]) * int(mul[2])
            start_index = current_index
    return result


# def main(problem_input: str) -> Any:
#    return
