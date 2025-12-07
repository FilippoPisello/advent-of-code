"""Solution for day 7 of Advent of Code 2025, by max."""

from typing import Any, List, Tuple
import copy


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]

    grid, splits = _split_grid(grid)

    return splits


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]

    grid, splits = _split_grid(grid)

    start_col = grid[0].index("S")
    starting_count = [0] * len(grid[0])
    counts = starting_count.copy()
    counts[start_col] = 1

    # Sweep through rows
    for row in range(1, len(grid)):
        next_counts = starting_count.copy()
        for col in range(len(grid[0])):
            # Straight down
            if grid[row][col] == "|":
                next_counts[col] += counts[col]

            # Split at tree
            if grid[row][col] == "^":
                if col - 1 >= 0 and grid[row][col - 1] == "|":
                    next_counts[col - 1] += counts[col]
                if col + 1 < len(grid[0]) and grid[row][col + 1] == "|":
                    next_counts[col + 1] += counts[col]

        counts = next_counts

    exits = grid[-1]
    total = sum(counts[col] for col in range(len(grid[0])) if exits[col] == "|")
    return total


def _split_grid(grid: List[List[str]]) -> Tuple[List[List[str]], int]:
    splits = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                grid[row + 1][col] = "|"
            elif grid[row][col] == "^" and grid[row - 1][col] == "|":
                grid[row][col - 1] = "|"
                grid[row][col + 1] = "|"
                splits += 1
            elif grid[row - 1][col] == "|":
                grid[row][col] = "|"

    return grid, splits
