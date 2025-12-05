"""Tests for day 5 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day5.filippo.solution import main_part_one, main_part_two, extract_unique_ranges

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            3,
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
            14,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected


@pytest.mark.parametrize(
    ("raw_ranges", "expected"),
    (
        (
            # Contained
            [(1, 10), (2, 5)],
            [(1, 10)],
        ),
        (
            # External
            [(1, 10), (12, 15)],
            [(1, 10), (12, 15)],
        ),
        (
            # Overlap
            [(1, 10), (9, 15)],
            [(1, 15)],
        ),
        (
            # Contained touches right
            [(1, 10), (9, 10)],
            [(1, 10)],
        ),
        (
            # Overlap touches left
            [(1, 10), (10, 15)],
            [(1, 15)],
        ),
        (
            # Mix up 1
            [(1, 10), (10, 15), (21, 34), (22, 30)],
            [(1, 15), (21, 34)],
        ),
    ),
)
def test_ranges_merging(raw_ranges, expected):
    assert extract_unique_ranges(raw_ranges) == expected
