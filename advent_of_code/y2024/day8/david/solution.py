"""Solution for day 8 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    antenna_map = problem_input.split("\n")
    antennas = []
    total = 0

    antennas = find_all_antenna(antenna_map)

    for antenna in antennas:
        for antenna_2 in antennas:
            if antenna[1] == antenna_2[1] and antenna_2[0] != antenna[0]:
                antenna_map, added = change_antenna_map(antenna_map, antenna, antenna_2)
                total += added
    return total


def change_antenna_map(map, antenna_1, antenna_2):
    rows = len(map) - 1
    cols = len(map[0]) - 1

    dist_row = abs(antenna_1[0][0] - antenna_2[0][0])
    dist_col = abs(antenna_1[0][1] - antenna_2[0][1])
    new_antenna_1 = []
    new_antenna_2 = []
    counter = 0
    order = []
    if antenna_1[0][0] < antenna_2[0][0]:
        order.append(1)
    else:
        order.append(2)

    if antenna_1[0][1] < antenna_2[0][1]:
        order.append(1)
    else:
        order.append(2)

    if order == [1, 1]:
        if antenna_1[0][0] - dist_row >= 0 and antenna_1[0][1] - dist_col >= 0:
            new_antenna_1 = [antenna_1[0][0] - dist_row, antenna_1[0][1] - dist_col]

        if antenna_2[0][0] + dist_row <= rows and antenna_2[0][1] + dist_col <= cols:
            new_antenna_2 = [antenna_2[0][0] + dist_row, antenna_2[0][1] + dist_col]

    if order == [2, 1]:
        if antenna_1[0][0] + dist_row <= rows and antenna_1[0][1] - dist_col >= 0:
            new_antenna_1 = [antenna_1[0][0] + dist_row, antenna_1[0][1] - dist_col]

        if antenna_2[0][0] - dist_row >= 0 and antenna_2[0][1] + dist_col <= cols:
            new_antenna_2 = [antenna_2[0][0] - dist_row, antenna_2[0][1] + dist_col]

    if order == [1, 2]:
        if antenna_1[0][0] - dist_row >= 0 and antenna_1[0][1] + dist_col <= cols:
            new_antenna_1 = [antenna_1[0][0] - dist_row, antenna_1[0][1] + dist_col]

        if antenna_2[0][0] + dist_row <= rows and antenna_2[0][1] - dist_col >= 0:
            new_antenna_2 = [antenna_2[0][0] + dist_row, antenna_2[0][1] - dist_col]

    if order == [2, 2]:
        if antenna_2[0][0] - dist_row >= 0 and antenna_2[0][1] - dist_col >= 0:
            new_antenna_2 = [antenna_2[0][0] - dist_row, antenna_2[0][1] - dist_col]

        if antenna_1[0][0] + dist_row <= rows and antenna_1[0][1] + dist_col <= cols:
            new_antenna_1 = [antenna_1[0][0] + dist_row, antenna_1[0][1] + dist_col]

    if new_antenna_1 != []:
        if map[new_antenna_1[0]][new_antenna_1[1]] != "ف":
            counter += 1
            map[new_antenna_1[0]] = (
                map[new_antenna_1[0]][: new_antenna_1[1]]
                + "ف"
                + map[new_antenna_1[0]][new_antenna_1[1] + 1 :]
            )

    if new_antenna_2 != []:
        if map[new_antenna_2[0]][new_antenna_2[1]] != "ف":
            counter += 1
            map[new_antenna_2[0]] = (
                map[new_antenna_2[0]][: new_antenna_2[1]]
                + "ف"
                + map[new_antenna_2[0]][new_antenna_2[1] + 1 :]
            )

    return map, counter


def find_all_antenna(map):
    antennas = []
    for row, line in enumerate(map):
        for col, char in enumerate(line):
            if char != ".":
                antennas.append([[row, col], char])
    return antennas


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
