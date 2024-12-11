"""Solution for day 10 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple
import copy


def main_part_one(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    grid = [list(map(int, line)) for line in inputs]

    trailheads = _parse_trailheads(grid, 9)
    ways = 0

    for trailhead in trailheads:
        ways += len(set(_parse_trailhead_options(grid, trailhead)))

    return ways


def _parse_trailheads(grid: List[List[str]], step: int) -> List[Tuple[int, int]]:
    steps = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):

            if grid[x][y] == step:
                steps.append((x, y))

    return steps


def _parse_trailhead_options(
    grid: List[List[str]], trailhead: Tuple[int, int]
) -> List[Tuple[int, int]]:
    steps = [8, 7, 6, 5, 4, 3, 2, 1, 0]

    for step in steps:
        starts = [copy.deepcopy(trailhead)] if step == 8 else copy.deepcopy(next_starts)
        next_starts = []

        for start in starts:
            successful_suroundings = _evaluate_suroundings(grid, start, step)
            for successful_surounding in successful_suroundings:
                next_starts.append(successful_surounding)

    return next_starts


def _evaluate_suroundings(
    grid: List[List[str]], start: Tuple[int, int], previous_step: int
) -> List[Tuple[int, int]]:
    paths = []

    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

    for direction in directions:
        x = start[0] + directions[direction][0]
        y = start[1] + directions[direction][1]

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == previous_step:
            paths.append((x, y))

    return paths


def main_part_two(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    grid = [list(map(int, line)) for line in inputs]

    trailheads = _parse_trailheads(grid, 9)
    ways = 0

    for trailhead in trailheads:
        ways += len(_parse_trailhead_options(grid, trailhead))

    return ways


# def main(problem_input: str) -> Any:
#    return
