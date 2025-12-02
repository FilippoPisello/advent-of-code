"""Solution for day 2 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    ranges = problem_input.split(",")
    sum_invalid = 0
    for id_range in ranges:
        range_start, range_end = map(int, id_range.split("-"))
        for id_ in range(range_start, range_end + 1):
            id_str = str(id_)
            if len(id_str) % 2 != 0:
                continue
            first_half, second_half = (
                id_str[: len(id_str) // 2],
                id_str[len(id_str) // 2 :],
            )
            if first_half == second_half:
                sum_invalid += id_
    return sum_invalid


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
