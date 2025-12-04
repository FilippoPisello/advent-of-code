"""Solution for day 3 of Advent of Code 2025, by sacha."""

from typing import Any


def main_part_one(problem_input: str) -> int:
    max_battery = 0
    for battery in problem_input.splitlines():
        max_volt = max(int(i) for i in battery[:-1])
        index_max = battery.find(str(max_volt))
        max2_volt = max(int(i) for i in battery[index_max + 1:])
        max_battery += 10*max_volt + max2_volt
    return max_battery


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
