"""Solution for day 8 of Advent of Code 2024, by filippo."""

import itertools
from functools import partial
from typing import Any, Callable

Coordinate = tuple[int, int]


def main(
    problem_input: str,
    antinodes_function: Callable[
        [tuple[Coordinate, Coordinate], int, int], set[Coordinate]
    ],
) -> Any:
    rows = problem_input.splitlines()
    max_x = len(rows[0])
    max_y = len(rows)

    unique_chars = _find_unique_chars(rows)
    antinodes = set()
    for char in unique_chars:
        locations = _find_locations(rows, char)
        pairs = _compute_possible_pairs(locations)
        for pair in pairs:
            antinodes_coordinates = antinodes_function(pair, max_x, max_y)
            antinodes.update(antinodes_coordinates)
    return len(antinodes)


def _find_unique_chars(rows: list[str]) -> set[str]:
    characters = set("".join(rows))
    characters.discard(".")
    characters.discard("#")
    return characters


def _find_locations(rows: list[str], char: str) -> list[Coordinate]:
    locations = []
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c == char:
                locations.append((x, y))
    return locations


def _compute_possible_pairs(
    coordinates: list[Coordinate],
) -> list[tuple[Coordinate, Coordinate]]:
    return list(itertools.combinations(coordinates, 2))


def _calculate_antinodes_coordinates_spot(
    pair: tuple[Coordinate, Coordinate], max_x: int, max_y: int
) -> set[Coordinate]:
    distances = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    first_antinode = (pair[1][0] + distances[0], pair[1][1] + distances[1])
    second_antinode = (pair[0][0] - distances[0], pair[0][1] - distances[1])
    return {
        antinode
        for antinode in (first_antinode, second_antinode)
        if _is_coordinate_in_bounds(antinode, max_x, max_y)
    }


def _calculate_antinodes_coordinates_line(
    pair: tuple[Coordinate, Coordinate], max_x: int, max_y: int
) -> set[Coordinate]:
    distances = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    antinodes = set(pair)

    for multiplier, starting_point in ((1, pair[1]), (-1, pair[0])):
        while True:
            antinode = (
                starting_point[0] + distances[0] * multiplier,
                starting_point[1] + distances[1] * multiplier,
            )
            if not _is_coordinate_in_bounds(antinode, max_x, max_y):
                break
            antinodes.add(antinode)
            multiplier += 1 if multiplier > 0 else -1

    return antinodes


def _is_coordinate_in_bounds(coordinate: Coordinate, max_x: int, max_y: int) -> bool:
    return (0 <= coordinate[0] < max_x) and (0 <= coordinate[1] < max_y)


main_part_one = partial(main, antinodes_function=_calculate_antinodes_coordinates_spot)
main_part_two = partial(main, antinodes_function=_calculate_antinodes_coordinates_line)

# def main(problem_input: str) -> Any:
#    return
