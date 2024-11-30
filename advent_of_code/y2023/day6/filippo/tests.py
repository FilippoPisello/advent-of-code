import pytest

from advent_of_code.day6.filippo.solution import (
    Race,
    main_part_one,
    main_part_two,
    parse_race_as_one,
    parse_races_from_lines,
)


def test_races_are_parsed_from_file():
    problem_input = [
        "Time:        44     82     69     81",
        "Distance:   202   1076   1138   1458",
    ]
    assert parse_races_from_lines(problem_input) == [
        Race(time=44, record_distance=202),
        Race(time=82, record_distance=1076),
        Race(time=69, record_distance=1138),
        Race(time=81, record_distance=1458),
    ]


@pytest.mark.parametrize(
    ("time", "record_distance", "expected"),
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
    ],
)
def test_number_of_options_calculation(time, record_distance, expected):
    assert Race(time, record_distance).winning_options() == expected


def test_example_part_one():
    problem_input = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    assert main_part_one(problem_input) == 288


def test_line_is_parsed_as_one():
    problem_input = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    assert parse_race_as_one(problem_input) == Race(time=71530, record_distance=940200)


def test_example_part_two():
    problem_input = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    assert main_part_two(problem_input) == 71503
