"""Solution for day 6 of Advent of Code 2024, by filippo."""

from typing import Any

DIRECTIONS = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}


def main_part_one(problem_input: str) -> Any:
    rows = problem_input.splitlines()
    current_coordinates = _find_starting_coordinates(rows)
    direction = "up"
    walked_coordinates = set()
    walked_coordinates.add(current_coordinates)

    while True:
        tentative_new_coordinates = _find_next_destination(
            current_coordinates, direction
        )
        if _is_out_of_bounds(rows, tentative_new_coordinates):
            break
        if _is_obstacle(rows, tentative_new_coordinates):
            direction = _turn_right(direction)
        else:
            current_coordinates = tentative_new_coordinates
            walked_coordinates.add(current_coordinates)

    return len(walked_coordinates)


def _find_next_destination(current_coordinates, direction):
    return (
        current_coordinates[0] + DIRECTIONS[direction][0],
        current_coordinates[1] + DIRECTIONS[direction][1],
    )


def _find_starting_coordinates(rows: list[str]) -> tuple[int, int]:
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)
    raise ValueError("Starting coordinates not found")


def _is_out_of_bounds(rows: list[str], coordinates: tuple[int, int]) -> bool:
    try:
        rows[coordinates[1]][coordinates[0]]
        return False
    except IndexError:
        return True


def _is_obstacle(rows: list[str], coordinates: tuple[int, int]) -> bool:
    return rows[coordinates[1]][coordinates[0]] == "#"


def _turn_right(direction: str) -> str:
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
