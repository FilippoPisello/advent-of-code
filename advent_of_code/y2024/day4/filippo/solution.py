"""Solution for day 4 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    count = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "X":
                continue
            count += int(_check_horizontal(line, x))
            count += int(_check_vertical(lines, x, y))
    return count


def _check_horizontal(line: str, x: int) -> bool:
    if line[x : x + 4] == "XMAS":
        return True
    if line[x - 3 : x + 1] == "SAMX":
        return True
    return False


def _check_vertical(lines: list[str], x: int, y: int) -> bool:
    try:
        indexes = [y + 1, y + 2, y + 3]
        letters = [lines[i][x] for i in indexes]
        if letters == ["M", "A", "S"]:
            return True
        reverse_indexes = [y - 1, y - 2, y - 3]
        reverse_letters = [lines[i][x] for i in reverse_indexes]
        if reverse_letters == ["S", "A", "M"]:
            return True
        return False
    except IndexError:
        return False


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
