"""Solution for day 2 of Advent of Code 2024, by david."""

from typing import Any
import re
import numpy as np


def main_part_one(problem_input: str) -> Any:
    counter = 0
    for line in problem_input.splitlines():
        splited_line = line.split()
        moving = 0
        last_number = 0

        for index, level in enumerate(splited_line):
            current_number = int(level)
            if index == 0:
                last_number = current_number

            elif index < len(splited_line):
                if (
                    current_number < last_number
                    and abs(current_number - last_number) < 4
                ):
                    if moving == 0:
                        moving = -1

                    elif moving == 1:
                        break

                    elif index == len(splited_line) - 1:
                        counter += 1

                elif (
                    current_number > last_number
                    and abs(current_number - last_number) < 4
                ):
                    if moving == 0:
                        moving = 1

                    elif moving == -1:
                        break

                    elif index == len(splited_line) - 1:
                        counter += 1

                else:
                    break

                last_number = current_number

    return counter


def main_part_two(problem_input: str) -> Any:

    counter = 0
    reports = problem_input.split("\n")

    for r in reports:
        report = np.array(re.findall(r"\d+", r), dtype=int)
        ### Below is actual proper answer to part 1 ###
        if actual_part_1_solution(report):
            counter += 1
            continue

        for i in range(len(report)):
            if i == 0:
                new_report = report[1:]
                if actual_part_1_solution(new_report):
                    counter += 1
                    break

            if i == len(report) - 1:
                new_report = report[:-1]
                if actual_part_1_solution(new_report):
                    counter += 1
                    break

            else:
                new_report = np.concatenate((report[:i], report[i + 1 :]))
                if actual_part_1_solution(new_report):
                    counter += 1
                    break

    return counter


def actual_part_1_solution(df: list[int]) -> bool:
    diff = np.diff(df)
    if np.all(diff > 0) or np.all(diff < 0):
        abso = np.absolute(diff)
        if np.all(abso > 0) and np.all(abso < 4):
            return True
        else:
            return False


# def main(problem_input: str) -> Any:
#    return
