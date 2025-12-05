"""Solution for day 5 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    ranges, ids = problem_input.split("\n\n")
    int_ranges = [tuple(map(int, line.split("-"))) for line in ranges.splitlines()]
    fresh_count = 0

    for id_ in map(int, ids.splitlines()):
        for start, end in int_ranges:
            if start <= id_ <= end:
                fresh_count += 1
                break

    return fresh_count


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
