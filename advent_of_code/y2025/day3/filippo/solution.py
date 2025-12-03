"""Solution for day 3 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    joltage = 0

    banks = problem_input.splitlines()
    for bank in banks:
        bank_record = 0
        batteries = [int(battery) for battery in list(bank)]
        highest_possible_ten = max(batteries[:-1])
        for index, battery in enumerate(batteries[:-1]):
            if battery == highest_possible_ten:
                higest_possible_unit = max(batteries[index + 1 :])
                possible_combination = int(
                    f"{highest_possible_ten}{higest_possible_unit}"
                )
                if possible_combination > bank_record:
                    bank_record = possible_combination
        joltage += bank_record
    return joltage


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
