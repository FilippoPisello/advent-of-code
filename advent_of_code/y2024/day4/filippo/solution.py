"""Solution for day 4 of Advent of Code 2024, by filippo."""

import re
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
    slices = []
    for x, _ in enumerate(rows[0]):
        _slice = ""
        for row in rows:
            _slice += row[x]
        slices.append(_slice)
    return slices


def _get_diagonal_slices(text: str) -> list[str]:
    rows = text.splitlines()
    slices = []
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
                if y > 0:
                    y -= 1
                else:
                    x += 1
                break
    return slices


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
