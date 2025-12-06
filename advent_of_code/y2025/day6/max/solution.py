"""Solution for day 6 of Advent of Code 2025, by max."""

from functools import total_ordering
from typing import Any
import math


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.split("\n")
    grid = [[char for char in line.split()] for line in lines]

    total = 0
    for col in range(len(grid[0])):
        operation = []
        operator = None

        for row in range(len(grid)):
            if grid[row][col].isdigit():
                operation.append(int(grid[row][col]))
            else:
                operator = grid[row][col]

        if operator == "+":
            result = sum(operation)
        elif operator == "*":
            result = math.prod(operation)
        else:
            raise ValueError(f"Invalid operator: {operator}")

        total += result

    return total


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.split("\n")
    grid = [[char for char in line] for line in lines]

    total = 0
    operation = []
    operator = None

    for col in range(len(grid[0])):
        operation_separator = 0
        current_number = ""

        for row in range(len(grid)):
            if grid[row][col].isdigit():
                current_number = current_number + grid[row][col]
            if grid[row][col] in ("+", "*"):
                operator = grid[row][col]
            if grid[row][col] in (" ", ""):
                operation_separator += 1

        if len(current_number) > 0:
            operation.append(int(current_number))

        if operation_separator == len(grid) or col == len(grid[0]) - 1:
            print(operation, operator)
            if operator == "+":
                result = sum(operation)
            elif operator == "*":
                result = math.prod(operation)
            else:
                raise ValueError(f"Invalid operator: {operator}")

            operation = []
            operator = None
            total += result

    return total
