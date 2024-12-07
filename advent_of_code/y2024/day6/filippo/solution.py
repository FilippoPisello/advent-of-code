"""Solution for day 6 of Advent of Code 2024, by filippo."""

from pathlib import Path
from time import sleep
from typing import Any

DIRECTIONS = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}
MAP_PATH = Path(__file__).resolve().parent / "map.txt"


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


def main_part_two(problem_input: str) -> Any:
    rows = problem_input.splitlines()

    loops_counter = 0

    #  Insert an obstacle in every empty cell and check if we are in a loop
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell == "#" or cell == "^":
                continue

            current_coordinates = _find_starting_coordinates(rows)
            direction = "up"
            walked_coordinates = set()
            walked_coordinates.add((current_coordinates, direction))
            alternative_map = _alter_map(rows, (x, y), "#")
            while True:
                tentative_new_coordinates = _find_next_destination(
                    current_coordinates, direction
                )
                # If we are about to get back to a point already visited, with
                # the same direction, we are in a loop
                if (tentative_new_coordinates, direction) in walked_coordinates:
                    loops_counter += 1
                    break
                if _is_out_of_bounds(alternative_map, tentative_new_coordinates):
                    break
                if _is_obstacle(alternative_map, tentative_new_coordinates):
                    direction = _turn_right(direction)
                else:
                    current_coordinates = tentative_new_coordinates
                    walked_coordinates.add((current_coordinates, direction))
    return loops_counter


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
    if (
        coordinates[1] < 0
        or coordinates[1] >= len(rows)
        or coordinates[0] < 0
        or coordinates[0] >= len(rows[0])
    ):
        return True
    return False


def _is_obstacle(rows: list[str], coordinates: tuple[int, int]) -> bool:
    return rows[coordinates[1]][coordinates[0]] == "#"


def _turn_right(direction: str) -> str:
    directions = list(DIRECTIONS.keys())
    return directions[(directions.index(direction) + 1) % len(directions)]


def write_map(
    rows: list[str],
    walked_coordinates: set[tuple[int, int]],
    current_coordinates: tuple[int, int],
    direction: str,
) -> list[str]:
    directions = {
        "up": "^",
        "right": ">",
        "down": "v",
        "left": "<",
    }
    map = rows.copy()
    for y, row in enumerate(rows):
        for x, _ in enumerate(row):
            if (x, y) == current_coordinates:
                map[y] = map[y][:x] + directions[direction] + map[y][x + 1 :]
            elif (x, y) in walked_coordinates or (
                (x, y),
                direction,
            ) in walked_coordinates:
                map[y] = map[y][:x] + "X" + map[y][x + 1 :]
    with open(MAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(map))
    return map


def _alter_map(
    rows: list[str], coordinates: tuple[int, int], character: str
) -> list[str]:
    return [
        (
            row[: coordinates[0]] + character + row[coordinates[0] + 1 :]
            if y == coordinates[1]
            else row
        )
        for y, row in enumerate(rows)
    ]


# def main(problem_input: str) -> Any:
#    return
