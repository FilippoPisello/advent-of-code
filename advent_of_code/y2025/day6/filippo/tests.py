"""Tests for day 6 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day6.filippo.solution import (
    main_part_one,
    main_part_two,
    recode_values,
    split_value_columns,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            4277556,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.skip(reason="Part two not implemented yet")
@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            3263827,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            [
                ["123", " 45", "  6"],
                ["328", "64 ", "98 "],
                [" 51", "387", "215"],
                ["64 ", "23 ", "314"],
            ],
        ),
    ),
)
def test_columns_splitting(problem_input, expected):
    assert split_value_columns(problem_input) == expected


@pytest.mark.skip(reason="Part two not implemented yet")
@pytest.mark.parametrize(
    ("raw_values", "expected"),
    (
        (
            [64, 23, 314],
            [623, 431, 4],
        ),
        (
            [51, 387, 215],
            [32, 581, 175],
        ),
    ),
)
def test_values_recoding(raw_values, expected):
    assert recode_values(raw_values) == expected
