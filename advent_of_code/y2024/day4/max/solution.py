"""Solution for day 1 of Advent of Code 2021, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    rows, columns = len(lines), len(lines[0])
    grid = [list(line) for line in lines]

    words_storage = []

    for i in range(rows):
        for y in range(columns):
            words_storage.extend(get_neighbors(grid, i, y))

    return words_storage.count("XMAS")


def get_neighbors(grid, row, col):

    directions = {
        "above": (-1, 0),
        "below": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "above_left": (-1, -1),
        "above_right": (-1, 1),
        "below_left": (1, -1),
        "below_right": (1, 1),
    }

    words = []

    for dr, dc in directions.values():
        word = [grid[row][col]]

        for z in range(1, 4):
            r, c = row + dr * z, col + dc * z

            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                word.append(grid[r][c])
            else:
                break

        if len(word) == 4:
            words.append("".join(word))

    return words


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    rows, columns = len(lines), len(lines[0])
    grid = [list(line) for line in lines]

    directions = {
        "above_left": (-1, -1),
        "below_right": (1, 1),
        "above_right": (-1, 1),
        "below_left": (1, -1),
    }

    words_storage = []

    for i in range(rows):
        for y in range(columns):
            if grid[i][y] == "A":
                words_storage.extend(get_neighbors2(grid, i, y))

    words_count = 0
    combinations = ["AMSMS", "AMSSM", "ASMMS", "ASMSM"]

    for combination in combinations:
        words_count += words_storage.count(combination)

    return words_count


def get_neighbors2(grid, row, col):

    directions = {
        "above_left": (-1, -1),
        "below_right": (1, 1),
        "above_right": (-1, 1),
        "below_left": (1, -1),
    }

    words = []

    word = [grid[row][col]]

    for dr, dc in directions.values():
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            word.append(grid[r][c])
        else:
            break

        if len(word) == 5:
            words.append("".join(word))

    return words


# def main_part_two(problem_input: str) -> Any:
#     lines = problem_input.splitlines()
#     trials = 0
#     matches = 0
#     for y, line in enumerate(lines[1:-1], start=1):
#         for x, char in enumerate(line[1:-1], start=1):
#             if char != "A":
#                 continue
#             try:
#                 trials+=1
#                 d1 = lines[y - 1][x - 1] + lines[y + 1][x + 1]
#                 d2 = lines[y - 1][x + 1] + lines[y + 1][x - 1]
#             except IndexError:
#                 continue
#             if (d1 == "MS" or d1 == "SM") and (d2 == "MS" or d2 == "SM"):
#                 matches += 1
#     return trials, matches

# def main(problem_input: str) -> Any:
#    return
