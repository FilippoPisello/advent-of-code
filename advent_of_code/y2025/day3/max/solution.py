"""Solution for day 3 of Advent of Code 2025, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    joltage = 0
    for bank in problem_input.splitlines():
        batteries = list(map(int, bank))
        first_digit = max(batteries[:-1])
        second_digit = max(batteries[batteries.index(first_digit) + 1 :])
        joltage += int(str(first_digit) + str(second_digit))

    return joltage


def main_part_two(problem_input: str) -> Any:
    joltage = 0
    for bank in problem_input.splitlines():
        batteries = list(map(int, bank))
        selected_batteries = []
        starting_index = 0

        for i in range(1, 13):
            batteries_to_check = batteries[starting_index : len(batteries) - 12 + i]
            top_battery = max(batteries_to_check)
            selected_batteries.append(top_battery)
            starting_index += batteries_to_check.index(top_battery) + 1

        joltage += int("".join(map(str, selected_batteries)))
    return joltage
