"""Solution for day 2 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    ranges = problem_input.split(",")
    sum_invalid = 0
    for id_range in ranges:
        range_start, range_end = map(int, id_range.split("-"))
        for id_ in range(range_start, range_end + 1):
            if _is_invalid_half_only(id_):
                sum_invalid += id_
    return sum_invalid


def _is_invalid_half_only(id_: int) -> bool:
    id_str = str(id_)
    if len(id_str) % 2 != 0:
        return False
    first_half, second_half = (
        id_str[: len(id_str) // 2],
        id_str[len(id_str) // 2 :],
    )
    return first_half == second_half


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
