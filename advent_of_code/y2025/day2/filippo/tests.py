"""Tests for day 2 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day2.filippo.solution import main_part_one, main_part_two

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (SAMPLE_INPUT_PATH.read_text(), 1227775554),
        ("11-22", 33),
        ("11-22,11-22", 66),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("95-115", 99 + 111),
        ("824824821-824824827", 824824824),
        (
            SAMPLE_INPUT_PATH.read_text(),
            4174379265,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
