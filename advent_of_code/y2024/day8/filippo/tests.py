"""Tests for day 8 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day8.filippo.solution import (
    _calculate_antinodes_coordinates_spot,
    main_part_one,
    main_part_two,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"
SAMPLE_INPUT_2_PATH = Path(__file__).resolve().parent / "sample_input_2.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            14,
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
            34,
        ),
        (
            SAMPLE_INPUT_2_PATH.read_text(),
            9,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
