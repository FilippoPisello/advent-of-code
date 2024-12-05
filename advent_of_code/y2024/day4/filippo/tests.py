import pytest

from advent_of_code.y2024.day4.filippo.solution import (
    _get_vertical_slices,
    main_part_one,
    main_part_two,
)


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        ("XMAS", 1),
        ("SAMX", 1),
        ("XXMAS", 1),
        ("XXMASS", 1),
        ("SAMX", 1),
        ("SSAMX", 1),
        (
            ("XXXX\n" + "MXXX\n" + "AXXX\n" + "SXXX"),
            1,
        ),
        (
            ("XXXX\n" + "XMXX\n" + "XXAX\n" + "XXXS"),
            1,
        ),
        (
            ("XXXX\n" + "XXMX\n" + "XAXX\n" + "SXXX"),
            1,
        ),
        (
            "MMMSXXMASM\n"
            + "MSAMXMSMSA\n"
            + "AMXSXMAAMM\n"
            + "MSAMASMSMX\n"
            + "XMASAMXAMM\n"
            + "XXAMMXXAMA\n"
            + "SMSMSASXSS\n"
            + "SAXAMASAAA\n"
            + "MAMMMXMMMM\n"
            + "MXMXAXMASX\n",
            18,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (
        (
            ("MXS\n" + "XAX\n" + "MXS\n"),
            1,
        ),
        (
            ("MXS\n" + "XAX\n" + "SXM\n"),
            0,
        ),
        (
            "MMMSXXMASM\n"
            + "MSAMXMSMSA\n"
            + "AMXSXMAAMM\n"
            + "MSAMASMSMX\n"
            + "XMASAMXAMM\n"
            + "XXAMMXXAMA\n"
            + "SMSMSASXSS\n"
            + "SAXAMASAAA\n"
            + "MAMMMXMMMM\n"
            + "MXMXAXMASX\n",
            9,
        ),
    ),
)
def test_cases_part_two(problem_input, expected):
    assert main_part_two(problem_input) == expected
