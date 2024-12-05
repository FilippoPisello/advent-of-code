"""Solution for day 4 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    word_search = problem_input.split("\n")
    total = 0
    for row, word in enumerate(word_search):
        for column in range(len(word)):
            if word[column] == "X":
                total += all_direction_word(column, row, word_search).count("XMAS")
    return total


def all_direction_word(column, row, puzzle):
    directions = {
        "N": (-1, 0),
        "NE": (-1, 1),
        "E": (0, 1),
        "SE": (1, 1),
        "S": (1, 0),
        "SW": (1, -1),
        "W": (0, -1),
        "NW": (-1, -1),
    }

    rows = len(puzzle)
    columns = len(puzzle[0])
    words = []

    for direction, (row_dir, col_dir) in directions.items():
        word = "X"
        r, c = row, column
        for i in range(3):
            r += row_dir
            c += col_dir
            if 0 <= r < rows and 0 <= c < columns:
                word += puzzle[r][c]
            else:
                break
        words.append(word)
    return words


def main_part_two(problem_input: str) -> Any:
    word_search = problem_input.split("\n")
    total = 0
    rows = len(word_search)
    columns = len(word_search[0])
    for r, word in enumerate(word_search):
        for c in range(len(word)):
            if word[c] == "A":
                if 0 < r < rows - 1 and 0 < c < columns - 1:
                    word_1 = (
                        word_search[r - 1][c - 1]
                        + word_search[r][c]
                        + word_search[r + 1][c + 1]
                    )
                    word_2 = (
                        word_search[r - 1][c + 1]
                        + word_search[r][c]
                        + word_search[r + 1][c - 1]
                    )
                    if word_1 in ("MAS", "SAM") and word_2 in ("MAS", "SAM"):
                        total += 1

    return total


# def main(problem_input: str) -> Any:
#    return
