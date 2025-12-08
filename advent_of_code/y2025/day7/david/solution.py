"""Solution for day 7 of Advent of Code 2025, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    manifold = format_input(problem_input)
    start_index = manifold[0].index("S")
    manifold[1][start_index] = "|"
    split_total = 0
    for row_index, row in enumerate(manifold[:]):
        for char_index, char in enumerate(row):
            if manifold[row_index - 1][char_index] == "|" and char == ".":
                manifold[row_index][char_index] = "|"
            elif manifold[row_index - 1][char_index] == "|" and char == "^":
                manifold[row_index][char_index - 1] = "|"
                manifold[row_index][char_index + 1] = "|"
                split_total += 1
    return split_total


def main_part_two(problem_input: str) -> Any:
    manifold = format_input(problem_input)
    start_index = manifold[0].index("S")
    manifold[1][start_index] = "|"
    split_total = 0
    num_rows = len(manifold)
    num_cols = len(manifold[0])

    quantum_grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    quantum_grid[1][start_index] = 1

    for row_index, row in enumerate(manifold[:]):
        for char_index, char in enumerate(row):
            if manifold[row_index - 1][char_index] == "|" and char in (".", "|"):
                manifold[row_index][char_index] = "|"
                quantum_grid[row_index][char_index] += quantum_grid[row_index - 1][
                    char_index
                ]
            elif manifold[row_index - 1][char_index] == "|" and char == "^":
                manifold[row_index][char_index - 1] = "|"
                quantum_grid[row_index][char_index - 1] += quantum_grid[row_index - 1][
                    char_index
                ]
                manifold[row_index][char_index + 1] = "|"
                quantum_grid[row_index][char_index + 1] += quantum_grid[row_index - 1][
                    char_index
                ]

    for value in quantum_grid[-1]:
        split_total += value

    return split_total


def format_input(input: str) -> Any:
    input_lines = input.splitlines()
    manifold = [list(line) for line in input_lines]
    return manifold


# def main(problem_input: str) -> Any:
#    return
