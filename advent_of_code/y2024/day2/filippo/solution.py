"""Solution for day 2 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    count_valid = 0

    for report in problem_input.splitlines():
        numbers = [int(x) for x in report.split(" ")]
        is_incremental = True
        is_decremental = True
        is_acceptable_difference = True
        for index in range(1, len(numbers)):
            if numbers[index] >= numbers[index - 1]:
                is_decremental = False
            elif numbers[index] <= numbers[index - 1]:
                is_incremental = False
            diff_with_previous = numbers[index] - numbers[index - 1]
            if (abs(diff_with_previous) > 3) or (abs(diff_with_previous) == 0):
                is_acceptable_difference = False
        if (is_incremental or is_decremental) and is_acceptable_difference:
            count_valid += 1
    return count_valid


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
