"""Tests for day 1 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day1.filippo.solution import main_part_one, main_part_two

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
        ("L68", 1),
        ("L168", 2),
        ("L150", 2),
        ("L149", 1),
        ("L151", 2),
        ("R25", 0),
        ("R49", 0),
        ("R50", 1),
        ("R51", 1),
        ("R55", 1),
        ("L50", 1),
        ("L50\nL100", 2),
        ("L68\nL30", 1),
        ("L68\nL30\nR48", 2),
        ("L68\nL30\nR48\nL5", 2),
        ("L68\nL30\nR48\nL5\nR60", 3),
        ("L68\nL30\nR48\nL5\nR60\nL55", 4),
        ("L68\nL30\nR48\nL5\nR60\nL55\nL1", 4),
        ("L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99", 5),
        ("L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14", 5),
        (SAMPLE_INPUT_PATH.read_text(), 6),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
