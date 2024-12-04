"""Solution for day 4 of Advent of Code 2024, by filippo."""

import re
from collections import Counter
from typing import Any


def main_part_one(problem_input: str) -> Any:
    problem_input = problem_input.replace(" ", "")
    slices = (
        _get_horizontal_slices(problem_input)
        + _get_vertical_slices(problem_input)
        + _get_diagonal_slices(problem_input)
    )
    count = 0
    for _slice in slices:
        count += len(re.findall("XMAS", _slice))
        count += len(re.findall("XMAS"[::-1], _slice))
    return count


def _get_horizontal_slices(text: str) -> list[str]:
    return text.splitlines()


def _get_vertical_slices(text: str) -> list[str]:
    rows = text.splitlines()
    return ["".join([row[x] for row in rows]) for x, _ in enumerate(rows[0])]


def _get_diagonal_slices(text: str) -> list[str]:
    rows = text.splitlines()
    slices = []
    # Start from the bottom left corner
    y = len(rows)
    x = 0
    while x <= len(rows[0]):
        _slice = ""
        _inverse_slice = ""
        i = 0
        while True:
            try:
                _slice += rows[y + i][x + i]
                _inverse_slice += rows[y + i][::-1][x + i]
                i += 1
            except IndexError:
                slices.append(_slice)
                slices.append(_inverse_slice)
                # When you get in 0, 0 you need to start moving right
                if y > 0:
                    y -= 1
                else:
                    x += 1
                break
    return slices


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    matches = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "A":
                continue
            try:
                square = [
                    lines[y - 1][x - 1 : x + 2],
                    lines[y][x - 1 : x + 2],
                    lines[y + 1][x - 1 : x + 2],
                ]
                slices = [
                    # Straight
                    square[0][1] + square[1][1] + square[2][1],
                    square[1][0] + square[1][1] + square[1][2],
                    # Diagonal
                    square[0][0] + square[1][1] + square[2][2],
                    square[0][2] + square[1][1] + square[2][0],
                ]
            except IndexError:
                continue
            inner_matches = 0
            for _slice in slices:
                inner_matches += int(_slice == "MAS" or _slice == "MAS"[::-1])
            if inner_matches >= 2:
                matches += 1
    return matches


# def main(problem_input: str) -> Any:
#    return
