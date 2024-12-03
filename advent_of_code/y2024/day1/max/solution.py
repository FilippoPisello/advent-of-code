"""Solution for day 1 of Advent of Code 2024, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    left_array, right_array = _parse_array(problem_input)

    left_array.sort()
    right_array.sort()

    sum = 0

    for i in range(len(left_array)):
        sum += abs(left_array[i] - right_array[i])

    return sum


def main_part_two(problem_input: str) -> Any:
    left_array, right_array = _parse_array(problem_input)

    sum = 0

    for number in left_array:
        sum += number * right_array.count(number)

    return sum


def _parse_array(input: str) -> tuple[list[int], list[int]]:
    lines = input.splitlines()

    left_array = []
    right_array = []

    for line in lines:

        left, right = line.split("  ")

        left_array.append(int(left))
        right_array.append(int(right))
    
    return left_array, right_array


# def main(problem_input: str) -> Any:
#    return
