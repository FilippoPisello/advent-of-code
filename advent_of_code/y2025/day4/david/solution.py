"""Solution for day 4 of Advent of Code 2025, by david. yes"""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(row) for row in lines]
    papers = 0
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

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            counter = 0
            if grid[i][j] == "@":
                for direction in directions.values():
                    if (
                        i + direction[0] < 0
                        or j + direction[1] < 0
                        or i + direction[0] >= len(grid)
                        or j + direction[1] >= len(grid[i])
                    ):
                        continue
                    else:
                        if grid[i + direction[0]][j + direction[1]] == "@":
                            counter += 1
                if counter < 4:
                    papers += 1

    print(papers)


def main_part_two(problem_input: str) -> Any:

    lines = problem_input.splitlines()
    grid = [list(row) for row in lines]
    papers = 0
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
    papers_last_loop = -1
    papers_this_loop = 0
    while papers_last_loop != papers_this_loop:
        papers_last_loop = papers_this_loop
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                counter = 0
                if grid[i][j] == "@":
                    for direction in directions.values():
                        if (
                            i + direction[0] < 0
                            or j + direction[1] < 0
                            or i + direction[0] >= len(grid)
                            or j + direction[1] >= len(grid[i])
                        ):
                            continue
                        else:
                            if grid[i + direction[0]][j + direction[1]] == "@":
                                counter += 1
                    if counter < 4:
                        papers_this_loop += 1
                        grid[i][j] = "#"

    print(papers_this_loop)
    return


# def main(problem_input: str) -> Any:
#    return
