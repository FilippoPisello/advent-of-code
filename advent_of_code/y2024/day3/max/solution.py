"""Solution for day 3 of Advent of Code 2024, by max."""

from typing import Any
import re


def main_part_one(problem_input: str) -> Any:
    inputs = _extract_mul_operations(problem_input)
    sum = 0

    for left, right in inputs:
        sum += left * right

    return sum


def main_part_two(problem_input: str) -> Any:
    inputs_raw = _filter_do_dont_entries(problem_input)
    sum = 0

    for input_raw in inputs_raw:
        inputs = _extract_mul_operations(input_raw)

        for left, right in inputs:
            sum += left * right

    return sum


def _extract_mul_operations(input_string: str) -> list[(int, int)]:
    mul_pattern = r"mul\((\d+),(\d+)\)"
    mul_matches = re.findall(mul_pattern, input_string)

    return [(int(a), int(b)) for a, b in mul_matches]


def _filter_do_dont_entries(input_string: str) -> list[str]:
    pattern_first_line = r"^(.*?)don\'t\(\)"
    pattern_other_lines = r"do\((.*?)(?=don\'t\(\))"

    return re.findall(pattern_first_line, input_string, re.DOTALL) + re.findall(
        pattern_other_lines, input_string, re.DOTALL
    )


# def main(problem_input: str) -> Any:
#    return
