"""Solution for day 9 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    coordinates = [
        tuple(map(int, line.split(","))) for line in problem_input.strip().splitlines()
    ]
    max_area = 0
    for index, (x1, y1) in enumerate(coordinates):
        for x2, y2 in coordinates[index + 1 :]:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area

    return max_area


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
