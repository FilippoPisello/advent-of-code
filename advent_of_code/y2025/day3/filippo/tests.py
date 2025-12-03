"""Tests for day 3 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day3.filippo.solution import main_part_one, main_part_two

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("987654321111111", 98),
        (SAMPLE_INPUT_PATH.read_text(), 357),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            3121910778619,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
