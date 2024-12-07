"""Solution for day 7 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    operations = problem_input.splitlines()

    valid = 0
    for operation in operations:
        wanted_result, factors = operation.split(": ")
        wanted_result = int(wanted_result)
        factors = [int(x) for x in factors.split(" ")]

        actual_result = [factors[0]]
        for factor in factors[1:]:
            actual_result = [x + factor for x in actual_result] + [
                x * factor for x in actual_result
            ]

        if wanted_result in actual_result:
            valid += wanted_result

    return valid


def main_part_two(problem_input: str) -> Any:
    operations = problem_input.splitlines()

    valid = 0
    for operation in operations:
        wanted_result, factors = operation.split(": ")
        wanted_result = int(wanted_result)
        factors = [int(x) for x in factors.split(" ")]

        actual_result = [factors[0]]
        for factor in factors[1:]:
            actual_result = (
                [x + factor for x in actual_result]
                + [x * factor for x in actual_result]
                + [int(str(x) + str(factor)) for x in actual_result]
            )

        if wanted_result in actual_result:
            valid += wanted_result

    return valid


# def main(problem_input: str) -> Any:
#    return
