"""Solution for day 6 of Advent of Code 2024, by max."""

from typing import Any
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


def _find_starting_point(grid: list[list[str]]) -> tuple[int, int]:
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "^":
                return row, column


def _change_direction(direction: str) -> tuple[int, int]:
    next_direction = {
        "top": "right",
        "right": "bottom",
        "bottom": "left",
        "left": "top",
    }

    return next_direction[direction]


def _explore(
    grid: list[list[str]],
    row: int,
    column: int,
    direction_row: int,
    direction_column: int,
) -> tuple[int, int]:
    row, column = row + direction_row, column + direction_column

    while (
        0 <= row < len(grid)
        and 0 <= column < len(grid[0])
        and (grid[row][column] in (".", "X", "^"))
    ):
        print(f"Coordinates row {row}, colum {column}, value {grid[row][column]}")
        grid[row][column] = "X"
        row += direction_row
        column += direction_column

    if not (0 <= row < len(grid) and 0 <= column < len(grid[0])):
        return row, column, grid, False

    return row - direction_row, column - direction_column, grid, True


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(line) for line in lines]
    directions = {"top": (-1, 0), "right": (0, 1), "bottom": (1, 0), "left": (0, -1)}

    direction = "top"
    start_row, start_column = _find_starting_point(grid)
    row, column = start_row, start_column
    direction_row, direction_column = directions[direction]
    can_explore = True
    loops_count = 0

    while can_explore:
        loops_count += _obstable(
            copy.deepcopy(grid), row, column, directions, start_row, start_column
        )

        if 0 <= row + direction_row < len(grid) and 0 <= column + direction_row < len(
            grid[0]
        ):
            if grid[row + direction_row][column + direction_column] in (".", "^"):
                row += direction_row
                column += direction_column

            else:
                direction = _change_direction(direction)
                direction_row, direction_column = directions[direction]

        else:
            can_explore = False

    return loops_count


def _obstable(start_grid, row, column, directions, start_row, start_column):
    loops_count = 0

    for obstable_row, obstacle_column in directions.values():
        grid = copy.deepcopy(start_grid)

        if not (
            0 <= row + obstable_row < len(grid)
            and 0 <= column + obstacle_column < len(grid[0])
        ):
            break

        grid[row + obstable_row][column + obstacle_column] = "0"

        direction = "top"
        direction_row, direction_column = directions[direction]
        can_explore = True
        node_count = 0

        while can_explore and node_count < 4:
            start_row, start_column, can_explore, node_count = _explore2(
                grid,
                start_row,
                start_column,
                direction_row,
                direction_column,
                node_count,
            )
            if can_explore:
                grid[start_row][start_column] = "+"
                direction = _change_direction(direction)
                direction_row, direction_column = directions[direction]

        if node_count > 3:
            loops_count += 1

    return loops_count


def _explore2(
    grid: list[list[str]],
    row: int,
    column: int,
    direction_row: int,
    direction_column: int,
    node_count: int,
) -> tuple[int, int]:
    row, column = row + direction_row, column + direction_column

    while (
        0 <= row < len(grid)
        and 0 <= column < len(grid[0])
        and (grid[row][column] in (".", "^", "+"))
    ):
        if grid[row][column] == "+":
            node_count += 1

        row += direction_row
        column += direction_column

    if not (0 <= row < len(grid) and 0 <= column < len(grid[0])):
        return row, column, False, node_count

    return row - direction_row, column - direction_column, True, node_count


# def main(problem_input: str) -> Any:
#    return
