"""Solution for day 4 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    n_rows = len(problem_input.splitlines())
    n_cols = len(problem_input.splitlines()[0])
    problem_input_list = [list(line) for line in problem_input.splitlines()]

    accesible_rolls = []

    for row, line in enumerate(problem_input.splitlines(), start=0):
        for col, char in enumerate(line):
            if char == "@":
                surroundings_positions = _generate_valid_surrounding_positions(
                    row, col, n_rows, n_cols
                )
                n_rolls = len(
                    [
                        (x, y)
                        for x, y in surroundings_positions
                        if _get_content_at_position(problem_input_list, x, y) == "@"
                    ]
                )
                if n_rolls < 4:
                    accesible_rolls.append((row, col))
    return len(accesible_rolls)


def _generate_valid_surrounding_positions(
    row: int, col: int, max_row: int, max_col: int
) -> list[tuple[int, int]]:
    all_positions = (
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    )
    return [(x, y) for x, y in all_positions if 0 <= x < max_row and 0 <= y < max_col]


def _get_content_at_position(
    problem_input_list: list[list[str]], row: int, col: int
) -> str:
    return problem_input_list[row][col]


def main_part_two(problem_input: str) -> Any:
    n_rows = len(problem_input.splitlines())
    n_cols = len(problem_input.splitlines()[0])
    problem_input_list = [list(line) for line in problem_input.splitlines()]

    accessible_rolls = []
    count_accessible_rolls_previous_lap = -1

    while len(accessible_rolls) != count_accessible_rolls_previous_lap:
        count_accessible_rolls_previous_lap = len(accessible_rolls)

        for row, line in enumerate(problem_input_list, start=0):
            for col, char in enumerate(line):
                if char == "@":
                    surroundings_positions = _generate_valid_surrounding_positions(
                        row, col, n_rows, n_cols
                    )
                    n_rolls = len(
                        [
                            (x, y)
                            for x, y in surroundings_positions
                            if _get_content_at_position(problem_input_list, x, y) == "@"
                        ]
                    )
                    if n_rolls < 4:
                        accessible_rolls.append((row, col))
                        problem_input_list[row][col] = "."

    return len(accessible_rolls)


# def main(problem_input: str) -> Any:
#    return
