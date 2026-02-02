"""Tests for day 5 of Advent of Code 2025."""

from pathlib import Path
import pytest
from solution import main_part_one, main_part_two


EXAMPLE_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part_one_example():
    """Test part one with example input."""
    result = main_part_one(EXAMPLE_INPUT)
    assert result == 3  # IDs 5, 11, and 17 are fresh


def test_part_two_example():
    """Test part two with example input."""
    result = main_part_two(EXAMPLE_INPUT)
    assert result == 14  # IDs: 3,4,5,10-20 = 14 total
