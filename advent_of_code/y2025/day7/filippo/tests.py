"""Tests for day 7 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day7.filippo.solution import (
    main_part_one,
    main_part_two,
    propagate_ray,
    propagate_timeline,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("previous_line", "line", "expected"),
    (
        (
            ".......|.......",
            "...............",
            ".......|.......",
        ),
        (
            "...|...|.......",
            "...............",
            "...|...|.......",
        ),
        (
            ".......|.......",
            ".......^.......",
            "......|^|......",
        ),
        (
            "..|^|^|||^|^|..",
            "...............",
            "..|.|.|||.|.|..",
        ),
    ),
)
def test_propagate_ray(previous_line, line, expected):
    assert propagate_ray(line, previous_line)[0] == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            21,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("line", "position", "expected"),
    (
        (
            "...............",
            6,
            [6],
        ),
    ),
)
def test_propagate_timeline(line, position, expected):
    assert propagate_timeline(line, position) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            40,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
