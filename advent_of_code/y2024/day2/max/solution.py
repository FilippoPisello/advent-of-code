"""Solution for day 2 of Advent of Code 2024, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    safe_lines_cnt = 0

    for line in lines:
        array = list(map(int, line.split(" ")))

        if _is_valid(array) is True:
            safe_lines_cnt += 1
                                    
    return safe_lines_cnt


def _is_valid(array: list) -> bool:
    array_difference = [int(array[i-1]) - int(array[i]) for i in range(1, len(array))]
    first_value_sign = 1 if array_difference[0] > 0 else -1
    return all(
            abs(difference) <= 3
                and (difference > 0) == (first_value_sign > 0)
                and difference != 0
                for difference in array_difference
        )
    
    
def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    safe_lines_cnt = main_part_one(problem_input)

    for line in lines:
        array = list(map(int, line.split(" ")))
        score = 0

        if _is_valid(array) is False:
            for index in range(len(array)):
                array_new = array[:index] + array[index + 1 :]
                if _is_valid(array_new) is True:
                    score = 1

        safe_lines_cnt += 1 if score > 0 else 0

    return safe_lines_cnt

# def main(problem_input: str) -> Any:
#    return
