import pytest

from advent_of_code.y2024.day3.filippo.solution import main_part_one, main_part_two


@pytest.mark.parametrize(
    ("problem_input", "expected"),
    (("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161),),
)
def test_cases_part_one(problem_input, expected):
    assert main_part_one(problem_input) == expected
