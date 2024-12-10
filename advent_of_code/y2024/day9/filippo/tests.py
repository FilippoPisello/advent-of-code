"""Tests for day 9 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day9.filippo.solution import (
    _compact,
    _compute_checksum,
    _decode,
    main_part_one,
    main_part_two,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            "12345",
            "0..111....22222",
        ),
        (
            "123451",
            "0..111....22222.",
        ),
        (
            "2333133121414131402",
            "00...111...2...333.44.5555.6666.777.888899",
        ),
        (
            "233313312141413140213",
            "00...111...2...333.44.5555.6666.777.888899.101010",
        ),
    ),
)
def test_decode(problem_input, expected):
    assert _decode(problem_input) == list(expected)


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            "00...111...2...333.44.5555.6666.777.888899",
            "0099811188827773336446555566..............",
        ),
        (
            [
                "0",
                "0",
                ".",
                ".",
                ".",
                "1",
                "1",
                "1",
                ".",
                ".",
                ".",
                "2",
                ".",
                ".",
                ".",
                "3",
                "3",
                "3",
                ".",
                "4",
                "4",
                ".",
                "5",
                "5",
                "5",
                "5",
                ".",
                "6",
                "6",
                "6",
                "6",
                ".",
                "7",
                "7",
                "7",
                ".",
                "8",
                "8",
                "8",
                "8",
                "9",
                "9",
                ".",
                "10",
                "10",
                "10",
            ],
            [
                "0",
                "0",
                "10",
                "10",
                "10",
                "1",
                "1",
                "1",
                "9",
                "9",
                "8",
                "2",
                "8",
                "8",
                "8",
                "3",
                "3",
                "3",
                "7",
                "4",
                "4",
                "7",
                "5",
                "5",
                "5",
                "5",
                "7",
                "6",
                "6",
                "6",
                "6",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
            ],
        ),
    ),
)
def test_shift_one_memory_unit(problem_input, expected):
    problem_input = list(problem_input)
    assert _compact(problem_input) == list(expected)


@pytest.mark.skip
def test_compute_checksum():
    assert _compute_checksum("0099811188827773336446555566..............") == 1928


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            SAMPLE_INPUT_PATH.read_text(),
            1928,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.skip(reason="Not implemented yet")
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
