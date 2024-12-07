"""Solution for day 7 of Advent of Code 2024, by david."""

from typing import Any
from functools import reduce


def main_part_one(problem_input: str) -> Any:
    puzzle = problem_input.split("\n")
    prob = []
    possible_equation = 0
    for equation in puzzle:
        results = int(equation.split(":")[0])
        numbers = list(map(int, equation.split(":")[1].split()))

        prob.append([results, numbers.copy()])

    for equation in prob:
        for i in range(len(equation[1]) - 1):
            new_total_list = []
            if i == 0:
                all_total_possible = [equation[1][0]]
            for total in all_total_possible:
                total_1 = total + equation[1][i + 1]
                total_2 = total * equation[1][i + 1]

                new_total_list.append(total_1)
                new_total_list.append(total_2)

            all_total_possible = new_total_list.copy()
        if equation[0] in all_total_possible:
            possible_equation += equation[0]

    return possible_equation


def main_part_two(problem_input: str) -> Any:
    puzzle = problem_input.split("\n")
    prob = []
    possible_equation = 0
    for equation in puzzle:
        results = int(equation.split(":")[0])
        numbers = list(map(int, equation.split(":")[1].split()))

        prob.append([results, numbers.copy()])

    for equation in prob:
        for i in range(len(equation[1]) - 1):
            new_total_list = []
            if i == 0:
                all_total_possible = [equation[1][0]]
            for total in all_total_possible:
                total_1 = total + equation[1][i + 1]
                total_2 = total * equation[1][i + 1]
                total_3 = int(str(total) + str(equation[1][i + 1]))
                new_total_list.append(total_1)
                new_total_list.append(total_2)
                new_total_list.append(total_3)
            all_total_possible = new_total_list.copy()
        if equation[0] in all_total_possible:
            possible_equation += equation[0]

    return possible_equation


# def main(problem_input: str) -> Any:
#    return
