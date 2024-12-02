"""Solution for day 2 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    count_valid = 0

    for report in problem_input.splitlines():
        numbers = [int(x) for x in report.split(" ")]
        count_valid += _is_report_valid(numbers)
    return count_valid


def _is_report_valid(numbers: list[int]) -> int:
    is_incremental = True
    is_decremental = True
    is_acceptable_difference = True
    for index in range(1, len(numbers)):
        if numbers[index] >= numbers[index - 1]:
            is_decremental = False
        elif numbers[index] <= numbers[index - 1]:
            is_incremental = False
        distance_from_previous = abs(numbers[index] - numbers[index - 1])
        if (distance_from_previous > 3) or (distance_from_previous == 0):
            is_acceptable_difference = False
    return int((is_incremental or is_decremental) and is_acceptable_difference)


def main_part_two(problem_input: str) -> Any:
    count_valid = 0

    for report in problem_input.splitlines():
        numbers = [int(x) for x in report.split(" ")]
        is_valid = [_is_report_valid(numbers)]
        for index in range(len(numbers)):
            alternative = numbers[:index] + numbers[index + 1 :]
            is_valid.append(_is_report_valid(alternative))
        count_valid += max(is_valid)

    return count_valid


# def main(problem_input: str) -> Any:
#    return
