"""Tests for day 9 of Advent of Code 2024, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2024.day9.filippo.solution import (
    _compute_checksum,
    _decode,
    _has_fillable_memory,
    _shift_one_memory_unit,
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
    ),
)
def test_decode(problem_input, expected):
    assert _decode(problem_input) == expected


def test_has_fillable_memory():
    assert _has_fillable_memory("0..111....22222") == True
    assert _has_fillable_memory("0..111....22222.") == True
    assert _has_fillable_memory("022111222......") == False


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            "0..111....22222",
            "02.111....2222.",
        ),
        (
            "02211122..2....",
            "022111222......",
        ),
        (
            "0099811188.2...333.44.5555.6666.777.8.....",
            "009981118882...333.44.5555.6666.777.......",
        ),
    ),
)
def test_shift_one_memory_unit(problem_input, expected):
    assert _shift_one_memory_unit(problem_input) == expected


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
