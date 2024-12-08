"""Solution for day 8 of Advent of Code 2024, by filippo."""

import itertools
from typing import Any

Coordinate = tuple[int, int]


def main_part_one(problem_input: str) -> Any:
    rows = problem_input.splitlines()

    unique_chars = _find_unique_chars(rows)
    antinodes = set()
    for char in unique_chars:
        locations = _find_locations(rows, char)
        pairs = _compute_possible_pairs(locations)
        for pair in pairs:
            antinodes_coordinates = _calculate_antinodes_coordinates(pair)
            for coordinate in antinodes_coordinates:
                if _is_coordinate_in_bounds(rows, coordinate):
                    antinodes.add(coordinate)
    return len(antinodes)


def _find_unique_chars(rows: list[str]) -> set[str]:
    characters = set("".join(rows))
    characters.discard(".")
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


def _calculate_antinodes_coordinates(
    pair: tuple[Coordinate, Coordinate]
) -> tuple[Coordinate, Coordinate]:
    distances = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    first_antinode = (pair[1][0] + distances[0], pair[1][1] + distances[1])
    second_antinode = (pair[0][0] - distances[0], pair[0][1] - distances[1])
    return [first_antinode, second_antinode]


def _is_coordinate_in_bounds(rows: list[str], coordinate: Coordinate) -> bool:
    return (0 <= coordinate[0] < len(rows[0])) and (0 <= coordinate[1] < len(rows))


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
