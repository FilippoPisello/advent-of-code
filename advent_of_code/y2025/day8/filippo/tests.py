"""Tests for day 8 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day8.filippo.solution import (
    main_part_one,
    main_part_two,
    parse_boxes,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


def test_box_parsing():
    problem_input = SAMPLE_INPUT_PATH.read_text()

    boxes = parse_boxes(problem_input)

    assert (162, 817, 812) in boxes
    assert boxes[(162, 817, 812)] is None
    assert len(boxes) == 20
    assert (425, 690, 689) in boxes
    assert boxes[(425, 690, 689)] is None


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            40,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input, 10) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            25272,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
