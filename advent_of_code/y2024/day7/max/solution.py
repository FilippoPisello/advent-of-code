"""Solution for day 7 of Advent of Code 2024, by max."""

from typing import Any, List


def main_part_one(problem_input: str) -> Any:
    sum_result = 0

    for calibration in problem_input.splitlines():
        test_value, numbers = calibration.split(":")
        equations = numbers.split()

        totals = generate_totals(int(equations[0]), equations, False)

        if int(test_value) in totals:
            sum_result += int(test_value)

    return sum_result


def generate_totals(start: int, equations: List[str], part2: bool) -> List[int]:
    totals = {start}

    for equation in equations[1:]:
        new_totals = set()
        equation = int(equation)

        for total in totals:
            new_totals.add(total + equation)
            new_totals.add(total * equation)
            if part2:
                new_totals.add(int(str(total) + str(equation)))

        totals = new_totals

    return list(totals)


def main_part_two(problem_input: str) -> Any:
    sum_result = 0

    for calibration in problem_input.splitlines():
        test_value, numbers = calibration.split(":")
        equations = numbers.split()

        totals = generate_totals(int(equations[0]), equations, True)

        if int(test_value) in totals:
            sum_result += int(test_value)

    return sum_result


# def main(problem_input: str) -> Any:
#    return
