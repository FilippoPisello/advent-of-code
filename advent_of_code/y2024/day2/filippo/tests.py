import pytest

from advent_of_code.y2024.day2.filippo.solution import main_part_one, main_part_two


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("7 6 4 2 1", 1),
        ("1 2 7 8 9", 0),
        ("9 7 6 2 1", 0),
        ("1 3 2 4 5", 0),
        ("8 6 4 4 1", 0),
        ("1 3 6 7 9", 1),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("7 6 4 2 1", 1),
        ("1 2 7 8 9", 0),
        ("9 7 6 2 1", 0),
        ("1 3 2 4 5", 1),
        ("8 6 4 4 1", 1),
        ("1 3 6 7 9", 1),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
