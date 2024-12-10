"""Solution for day 10 of Advent of Code 2024, by filippo."""

from typing import Any

Coordinates = tuple[int, int]


def main_part_one(problem_input: str) -> Any:
    rows = problem_input.splitlines()
    trailheads_coordinates = _find_trailheads(rows)

    total_score = 0
    for x, y in trailheads_coordinates:
        reachable_peaks = _find_reachable_peaks(x, y, rows)
        total_score += len(reachable_peaks)
    return total_score


def _find_trailheads(rows: list[str]) -> list[Coordinates]:
    return [(x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c == "0"]


def _find_reachable_peaks(
    start_x: int, start_y: int, rows: list[str]
) -> set[Coordinates]:
    reachable_peaks = set()

    walked_locations = {(start_x, start_y)}
    current_locations = {(start_x, start_y)}
    while current_locations:
        for x, y in current_locations.copy():

            for direct in DIRECTIONS:
                target_location = (x + direct[0], y + direct[1])
                if _is_out_of_bounds(rows, target_location):
                    continue
                if target_location in walked_locations:
                    continue

                # In test cases there might be a dot instead of a number, not
                # a valid location
                try:
                    target_height = int(rows[target_location[1]][target_location[0]])
                except ValueError:
                    continue

                current_height = int(rows[y][x])
                if target_height - current_height == 1:
                    if target_height == 9:
                        reachable_peaks.add(target_location)
                    walked_locations.add(target_location)
                    current_locations.add(target_location)
                else:
                    continue

            current_locations.remove((x, y))

    return reachable_peaks


DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def _is_out_of_bounds(rows: list[str], coordinates: tuple[int, int]) -> bool:
    if (
        coordinates[1] < 0
        or coordinates[1] >= len(rows)
        or coordinates[0] < 0
        or coordinates[0] >= len(rows[0])
    ):
        return True
    return False


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
