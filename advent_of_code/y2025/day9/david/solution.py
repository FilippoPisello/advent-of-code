"""Solution for day 9 of Advent of Code 2025, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    tiles_pairs = create_tiles_pair(problem_input)
    longest_square = calculate_longest_square(tiles_pairs)
    return longest_square


def main_part_two(problem_input: str) -> Any:
    return


def create_tiles_pair(problem_input: str) -> list:

    input_lines = problem_input.splitlines()
    tiles_pair_set = []
    for tile1, tile1_xy in enumerate(input_lines):
        for tile2_xy in input_lines[tile1 + 1 :]:
            tiles_pair_set.append([tile1_xy.split(","), tile2_xy.split(",")])

    return tiles_pair_set


def calculate_longest_square(tiles_pairs: list) -> int:
    longest_square = 0
    for tiles_pair in tiles_pairs:
        x1, y1 = map(int, tiles_pair[0])
        x2, y2 = map(int, tiles_pair[1])
        side_length = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if side_length > longest_square:
            longest_square = side_length
    return longest_square


# def main(problem_input: str) -> Any:
#    return
