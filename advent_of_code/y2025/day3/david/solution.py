"""Solution for day 3 of Advent of Code 2025, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    banks = problem_input.splitlines()
    joltage = 0
    for bank in banks:
        joltages = list(bank)
        joltages = [int(i) for i in joltages]
        first_digit_index = joltages[:-1].index(max(joltages[:-1]))
        first_digit = max(joltages[:-1])
        second_digit = max(joltages[first_digit_index + 1 :])
        joltage += int(str(first_digit) + str(second_digit))
    print(joltage)
    return


def main_part_two(problem_input: str) -> Any:
    banks = problem_input.splitlines()
    joltage = 0
    for bank in banks:
        joltages = list(bank)
        joltages = [int(i) for i in joltages]
        joltage_str = ""
        last_digit_index = 0
        for battery_nb in range(1, 13):
            if battery_nb == 1:
                last_digit_index = joltages[: -12 + battery_nb].index(
                    max(joltages[: -12 + battery_nb])
                )
                last_digit = max(joltages[: -12 + battery_nb])
            elif battery_nb < 12:
                last_digit_index += (
                    joltages[last_digit_index + 1 : -12 + battery_nb].index(
                        max(joltages[last_digit_index + 1 : -12 + battery_nb])
                    )
                    + 1
                )
                last_digit = max(joltages[last_digit_index : -12 + battery_nb])
            else:
                last_digit = max(joltages[last_digit_index + 1 :])
            joltage_str += str(last_digit)
        joltage += int(joltage_str)
    print(joltage)
    return


# def main(problem_input: str) -> Any:
#    return
