"""Solution for day 10 of Advent of Code 2024, by david."""

from typing import Any
import numpy as np


def main_part_one(problem_input: str) -> Any:
    data = process_problem_input(problem_input)
    zero_positions = find_zero(data)
    total_route_found = route(data, zero_positions)
    return total_route_found


def process_problem_input(problem_input: str) -> tuple:
    return [[int(num) for num in line.strip()] for line in problem_input.split("\n")]


def find_zero(data: list) -> int:
    pos = []
    for i, line in enumerate(data):
        for j, track in enumerate(line):
            if track == 0:
                pos.append([i, j])
    return pos


def route(data: list, zero_positions: list) -> int:
    total = 0
    for po in zero_positions:
        current = [po]
        all_current = []
        for i in range(8):
            all_current.append(current)
            current = []
            for pos in all_current:
                current += find_position(data, pos, i + 1)
                print(current)
            all_current = []
        total += len(current)
    return total


def find_position(data: list, po: list, i: int) -> list | bool:
    direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    all_pos = []
    for j in range(3):
        if 0 <= po[0] + direction[j][0] < len(data) and 0 <= po[1] + direction[j][
            1
        ] < len(data[0]):
            if data[po[0] + direction[j][0]][po[1] + direction[j][1]] == i:
                all_pos.append([po[0] + direction[j][0], po[1] + direction[j][1]])
    return all_pos


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
