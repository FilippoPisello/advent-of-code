"""Solution for day 6 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple
import copy


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]
    directions = {"top": (-1, 0), "right": (0, 1), "bottom": (1, 0), "left": (0, -1)}

    direction = "top"
    row, column = _find_starting_point(grid)
    direction_row, direction_column = directions[direction]
    can_explore = True

    while can_explore:
        row, column, grid, can_explore = _explore(
            grid, row, column, direction_row, direction_column
        )
        direction = _change_direction(direction)
        direction_row, direction_column = directions[direction]

    return sum(row.count("X") for row in grid)


def _find_starting_point(grid: List[List[str]]) -> Tuple[int, int]:
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "^":
                return row, column


def _change_direction(direction: str) -> Tuple[int, int]:
    next_direction = {
        "top": "right",
        "right": "bottom",
        "bottom": "left",
        "left": "top",
    }

    return next_direction[direction]


def _is_valid(grid: List[List[int]], row: int, column: int) -> bool:
    if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
        return True
    return False


def _explore(
    grid: list[list[str]],
    row: int,
    column: int,
    direction_row: int,
    direction_column: int,
) -> Tuple[int, int]:

    row, column = row + direction_row, column + direction_column

    while _is_valid(grid, row, column) and (grid[row][column] in (".", "X", "^")):
        grid[row][column] = "X"
        row += direction_row
        column += direction_column

    if not (_is_valid(grid, row, column)):
        return row, column, grid, False

    return row - direction_row, column - direction_column, grid, True


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]

    loops_count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            loops_count += _explore2(grid, x, y)

    return loops_count


def _explore2(grid, x, y):
    directions = {"top": (-1, 0), "right": (0, 1), "bottom": (1, 0), "left": (0, -1)}
    explored = set()
    new_grid = [row[:] for row in grid]

    if new_grid[x][y] == "^":
        return 0

    new_grid[x][y] = "#"

    row, column = _find_starting_point(new_grid)
    direction = "top"
    direction_row, direction_column = directions[direction]

    while True:
        row += direction_row
        column += direction_column

        current_state = ((row, column), direction)
        if current_state in explored:
            return 1

        if not _is_valid(new_grid, row, column):
            return 0

        if new_grid[row][column] in (".", "^"):
            explored.add(current_state)
        else:
            row -= direction_row
            column -= direction_column
            direction = _change_direction(direction)
            direction_row, direction_column = directions[direction]


# def main(problem_input: str) -> Any:
#    return
