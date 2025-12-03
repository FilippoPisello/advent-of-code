"""Solution for day 3 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    return _solver(problem_input, 2)


def main_part_two(problem_input: str) -> Any:
    return _solver(problem_input, 12)


def _solver(problem_input: str, number_of_digits: int) -> Any:
    joltage = 0

    banks = problem_input.splitlines()
    for bank in banks:
        bank_record = ""
        starting_index = 0
        batteries = [int(battery) for battery in list(bank)]

        for index in range(1, number_of_digits + 1):
            if index == number_of_digits:
                highest_possible_digit = max(batteries[starting_index:])
            else:
                highest_possible_digit = max(
                    batteries[starting_index : -(number_of_digits - index)]
                )
            starting_index = batteries.index(highest_possible_digit, starting_index) + 1
            bank_record += str(highest_possible_digit)

        joltage += int(bank_record)

    return joltage


# def main(problem_input: str) -> Any:
#    return
