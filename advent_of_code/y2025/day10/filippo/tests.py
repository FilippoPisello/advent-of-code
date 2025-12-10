"""Tests for day 10 of Advent of Code 2025, by filippo."""

from pathlib import Path

import pytest

from advent_of_code.y2025.day10.filippo.solution import (
    apply_button,
    main_part_one,
    main_part_two,
    parse_buttons,
)

SAMPLE_INPUT_PATH = Path(__file__).resolve().parent / "sample_input.txt"


@pytest.mark.parametrize(
    ("config", "expected"),
    (
        (
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            {(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)},
        ),
        (
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
            {(0, 1, 2, 3, 4), (0, 3, 4), (0, 1, 2, 4, 5), (1, 2)},
        ),
    ),
)
def test_parse_buttons(config, expected):
    assert parse_buttons(config) == expected


@pytest.mark.parametrize(
    ("state", "button", "expected"),
    (
        ("....", (3,), "...#"),
        ("...#", (3,), "...."),
        ("....", (1, 2), ".##."),
    ),
)
def test_apply_buttons(state, button, expected):
    assert apply_button(state, button) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}", 2),
        ("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}", 3),
        ("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}", 2),
        (SAMPLE_INPUT_PATH.read_text(), 7),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.skip("Remove this line once part two is implemented")
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
