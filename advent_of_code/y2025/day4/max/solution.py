"""Solution for day 4 of Advent of Code 2025, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]

    grid, accessible_rolls_count = _get_rolls(grid)

    return accessible_rolls_count


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]

    accessible_rolls_count = 0

    while True:
        grid, round_accessible_rolls_count = _get_rolls(grid)

        grid = [["." if cell == "x" else cell for cell in row] for row in grid]
        accessible_rolls_count += round_accessible_rolls_count

        if round_accessible_rolls_count == 0:
            break

    return accessible_rolls_count


def _get_rolls(grid: list[list[str]]) -> Any:
    adjacent_positions = {
        "above": (-1, 0),
        "below": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "above_left": (-1, -1),
        "above_right": (-1, 1),
        "below_left": (1, -1),
        "below_right": (1, 1),
    }

    accessible_rolls_count = 0

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == "@":
                adjacent_rolls_count = 0

                for direction, position in adjacent_positions.items():
                    x = row_index + position[0]
                    y = col_index + position[1]

                    try:
                        if grid[x][y] in ("@", "x") and x >= 0 and y >= 0:
                            adjacent_rolls_count += 1
                    except IndexError:
                        continue

                if adjacent_rolls_count < 4:
                    accessible_rolls_count += 1
                    grid[row_index][col_index] = "x"

    return grid, accessible_rolls_count


# def main(problem_input: str) -> Any:
#    return
