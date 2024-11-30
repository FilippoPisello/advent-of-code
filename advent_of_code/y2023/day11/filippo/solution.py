import re
from dataclasses import dataclass
from typing import ClassVar, Self


def main_part_one(problem_input: list[str]):
    empty_rows = _find_empty_rows(problem_input)
    empty_columns = _find_empty_columns(problem_input)
    galaxies = _parse_galaxies(problem_input)
    Galaxy.EXPANSION_COEFFICIENT = 2 - 1
    return _sum_shortest_distances(galaxies, empty_rows, empty_columns)


def main_part_two(problem_input: list[str]):
    empty_rows = _find_empty_rows(problem_input)
    empty_columns = _find_empty_columns(problem_input)
    galaxies = _parse_galaxies(problem_input)
    Galaxy.EXPANSION_COEFFICIENT = 1000000 - 1
    return _sum_shortest_distances(galaxies, empty_rows, empty_columns)


@dataclass
class Galaxy:
    x: int
    y: int
    EXPANSION_COEFFICIENT: ClassVar[int] = 0

    def distance(
        self, other: Self, empty_rows: set[str], empty_columns: set[str]
    ) -> int:
        x_dist = abs(self.x - other.x)
        y_dist = abs(self.y - other.y)
        for index in empty_rows:
            if min(self.y, other.y) < index < max(self.y, other.y):
                y_dist += self.EXPANSION_COEFFICIENT
        for index in empty_columns:
            if min(self.x, other.x) < index < max(self.x, other.x):
                x_dist += self.EXPANSION_COEFFICIENT
        return x_dist + y_dist


def _find_empty_rows(problem_input: list[str]) -> set[str]:
    return {index for index, row in enumerate(problem_input) if "#" not in row}


def _find_empty_columns(problem_input: list[str]) -> set[str]:
    indexes = set()
    for index, _ in enumerate(problem_input[0]):
        column = [row[index] for row in problem_input]
        if "#" not in column:
            indexes.add(index)
    return indexes


def _parse_galaxies(expanded_input: list[str]) -> list[Galaxy]:
    galaxies = []
    expr = re.compile(r"#")
    for y, line in enumerate(expanded_input):
        for match in expr.finditer(line):
            galaxies.append(Galaxy(match.span()[0], y))
    return galaxies


def _sum_shortest_distances(
    galaxies: list[Galaxy], empty_rows: set[str], empty_columns: set[str]
) -> int:
    distance = 0
    for index, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[index:]:
            distance += galaxy.distance(other_galaxy, empty_rows, empty_columns)
    return distance
