"""Solution for day 7 of Advent of Code 2024, by filippo."""

from functools import partial
from typing import Callable


def main(
    problem_input: str,
    operations: list[Callable[[list[int], int], list[int]]],
) -> int:
    equations = problem_input.splitlines()

    valid = 0
    for equation in equations:
        wanted_result, factors = equation.split(": ")
        wanted_result = int(wanted_result)
        factors = [int(x) for x in factors.split(" ")]

        actual_result = [factors[0]]
        for factor in factors[1:]:
            actual_result = sum(
                (operation(actual_result, factor) for operation in operations), []
            )

        if wanted_result in actual_result:
            valid += wanted_result

    return valid


def _sum(current_totals: list[int], factor: int) -> list[int]:
    return [x + factor for x in current_totals]


def _multiply(current_totals: list[int], factor: int) -> list[int]:
    return [x * factor for x in current_totals]


def _concatenate(current_totals: list[int], factor: int) -> list[int]:
    return [int(str(x) + str(factor)) for x in current_totals]


main_part_one = partial(
    main,
    operations=[_sum, _multiply],
)

main_part_two = partial(
    main,
    operations=[_sum, _multiply, _concatenate],
)
