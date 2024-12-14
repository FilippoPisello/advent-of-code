"""Solution for day 13 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple
import re, math


def main_part_one(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    button_a, button_b, prizes = _parse_input([input for input in inputs if input])

    tokens = 0

    for i in range(len(prizes)):
        tokens += _solve_equation(button_a[i], button_b[i], prizes[i], 0)

    return tokens


def _parse_input(inputs: List[str]) -> Tuple[dict, dict, dict]:
    button_a = {}
    button_b = {}
    prize = {}

    row = 0

    for input in inputs:
        raw_x, raw_y = tuple(re.findall(r"\d+", input))
        x, y = int(raw_x), int(raw_y)

        if "A" in input:
            button_a[row] = (x, y)
        elif "B" in input:
            button_b[row] = (x, y)
        elif "Prize" in input:
            prize[row] = (x, y)
            row += 1
        else:
            continue

    return button_a, button_b, prize


def _solve_equation(
    button_a: Tuple[int, int],
    button_b: Tuple[int, int],
    prize: Tuple[int, int],
    add: int,
) -> int:
    buttons = [
        [button_a[0], button_b[0]],
        [button_a[1], button_b[1]],
    ]

    prize = [prize[0] + add, prize[1] + add]

    # Check if the system is solvable
    det = buttons[0][0] * buttons[1][1] - buttons[0][1] * buttons[1][0]

    if det == 0:
        return 0

    equation_a = (prize[0] * buttons[1][1] - prize[1] * buttons[0][1]) / det
    equation_b = (prize[1] * buttons[0][0] - prize[0] * buttons[1][0]) / det

    if equation_a == round(equation_a) and equation_b == round(equation_b):
        return int(equation_a * 3 + equation_b)

    return 0


def main_part_two(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    button_a, button_b, prizes = _parse_input([input for input in inputs if input])

    tokens = 0
    print(len(prizes))

    for i in range(len(prizes)):
        tokens += _solve_equation(button_a[i], button_b[i], prizes[i], 10000000000000)

    return tokens


# def main(problem_input: str) -> Any:
#    return
