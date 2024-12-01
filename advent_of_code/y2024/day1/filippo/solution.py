"""Solution for day 1 of Advent of Code 2024, by filippo."""

from collections import Counter
from typing import Any


def main_part_one(problem_input: str) -> Any:
    left_list, right_list = _parse_input_to_left_right_lists(problem_input)
    return sum(
        abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list))
    )


def _parse_input_to_left_right_lists(problem_input) -> tuple[list[int], list[int]]:
    left_list, right_list = [], []
    for line in problem_input.splitlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list


def main_part_two(problem_input: str) -> Any:
    left_list, right_list = _parse_input_to_left_right_lists(problem_input)
    right_counter = Counter(right_list)
    result = 0
    for number in left_list:
        try:
            occurrence = right_counter[number]
        except KeyError:
            occurrence = 0
        result += number * occurrence
    return result
