"""Tests for day 11 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day11.filippo.solution import (
    main,
    main_part_one,
    main_part_two,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected", "iterations"),
    (
        (
            "125 17",
            3,
            1,
        ),
    ),
)
def test_cases_manual(problem_input, expected, iterations):
    assert main(problem_input, iterations) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            "125 17",
            55312,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected
