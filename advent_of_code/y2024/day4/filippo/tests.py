import pytest

from advent_of_code.y2024.day4.filippo.solution import main_part_one, main_part_two


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
            """
         XXXX
         MXXX
         AXXX
         SXXX
         """,
            1,
        ),
        (
            """
            MMMSXXMASM
            MSAMXMSMSA
            AMXSXMAAMM
            MSAMASMSMX
            XMASAMXAMM
            XXAMMXXAMA
            SMSMSASXSS
            SAXAMASAAA
            MAMMMXMMMM
            MXMXAXMASX
            """,
            18,
        ),
    ),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected
