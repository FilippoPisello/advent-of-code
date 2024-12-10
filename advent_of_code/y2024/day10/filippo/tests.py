"""Tests for day 10 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day10.filippo.solution import main_part_one, main_part_two

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"
SAMPLE_INPUT_PATH_2 = Path(__file__).resolve().parent / "sample_input2.txt"
SAMPLE_INPUT_PATH_3 = Path(__file__).resolve().parent / "sample_input3.txt"
SAMPLE_INPUT_PATH_4 = Path(__file__).resolve().parent / "sample_input4.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            36,
        ),
        (
            SAMPLE_INPUT_PATH_2.read_text(),
            1,
        ),
        (
            SAMPLE_INPUT_PATH_3.read_text(),
            2,
        ),
        (
            SAMPLE_INPUT_PATH_4.read_text(),
            4,
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
            "expected_result_part_one",
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
