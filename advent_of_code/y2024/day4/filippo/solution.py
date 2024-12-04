"""Solution for day 4 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = "XMAS".splitlines()
    count = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "X":
                continue
            indexes_to_check = (
                ((1, 0), (2, 0), (3, 0)),
                ((-1, 0), (-2, 0), (-3, 0)),
                ((0, 1), (0, 2), (0, 3)),
                ((0, -1), (0, -2), (0, -3)),
                ((1, 1), (2, 2), (3, 3)),
                ((-1, -1), (-2, -2), (-3, -3)),
                ((1, -1), (2, -2), (3, -3)),
                ((-1, 1), (-2, 2), (-3, 3)),
            )
            count += _check_indexes(lines, x, y, indexes_to_check)
    return count


def _check_indexes(
    lines: list[str],
    x: int,
    y: int,
    variations: tuple[tuple[tuple[int, int], ...], ...],
) -> int:
    count = 0
    for variation in variations:
        indexes = [(x + i, y + j) for i, j in variation]
        try:
            letters = [lines[j][i] for i, j in indexes]
            if letters == ["M", "A", "S"]:
                count += 1
        except IndexError:
            continue
    return count


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
