"""Tests for day 7 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day7.filippo.solution import main_part_one, main_part_two

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            3749,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            11387,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
