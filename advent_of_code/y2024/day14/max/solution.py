"""Solution for day 14 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple, Dict
from pathlib import Path
import re
from PIL import Image

DIR = Path("advent_of_code/y2024/day14/max/output")


def main_part_one(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    robots = _parse_input(inputs)

    final_positions = {}
    x_len = 100
    y_len = 102
    seconds = 100

    for robot in robots:
        final_positions[robot] = _seconds(robots[robot], seconds, x_len, y_len)

    square_1, square_2, square_3, square_4 = _assign_robots(final_positions, x_len, y_len)
    return square_1 * square_2 * square_3 * square_4

def _parse_input(inputs: List[str]) -> Dict[Tuple, Tuple]:
    robots = {}

    for i, input in enumerate(inputs, start=1):
        pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r"-?\d+", input))
        robots[i] = {
            "position": (pos_x, pos_y),
            "velocity": (vel_x, vel_y),
        }

    return robots

def _seconds(robot: Dict[Tuple[int, int], Tuple[int, int]], seconds: int, x_len: int, y_len: int) -> Tuple[int, int]:
    pos_x, pos_y = robot["position"]
    vel_x, vel_y = robot["velocity"]

    for second in range(seconds):
        pos_x += vel_x
        pos_y += vel_y

        if pos_x > x_len:
            pos_x -= (x_len + 1)
        elif pos_x < 0:
            pos_x += (x_len + 1)

        if pos_y > y_len:
            pos_y -= (y_len + 1)
        elif pos_y < 0:
            pos_y += (y_len + 1)

    return (pos_x, pos_y)

def _assign_robots(final_positions: Dict[int, Tuple[int, int]], x_len: int, y_len: int) -> Tuple[int, int, int, int]:
    a, b, c, d = 0, 0, 0, 0
    
    for robot in final_positions:

        if final_positions[robot][0] == x_len / 2 or final_positions[robot][1] == y_len / 2:
            continue

        if final_positions[robot][0] < x_len / 2:
            if final_positions[robot][1] < y_len / 2:
                a += 1
            else: 
                b += 1
        else:
            if final_positions[robot][1] < y_len / 2:
                c += 1
            else: 
                d += 1
        
    return a, b, c, d


def main_part_two(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    robots = _parse_input(inputs)

    x_len = 100
    y_len = 102
    seconds = 10000

    for second in range(seconds):
        robots = _second(robots, x_len, y_len)
        _draw_christmas_tree(robots, x_len, y_len, second)
    
    return 'Explore the output to find the Christmas tree.'

def _second(robots: Dict[Tuple[int, int], Tuple[int, int]], x_len: int, y_len: int) -> Dict[Tuple[int, int], Tuple[int, int]]:
    for robot in robots:
        pos_x, pos_y = robots[robot]["position"]
        vel_x, vel_y = robots[robot]["velocity"]

        pos_x += vel_x
        pos_y += vel_y

        if pos_x > x_len:
            pos_x -= (x_len + 1)
        elif pos_x < 0:
            pos_x += (x_len + 1)

        if pos_y > y_len:
            pos_y -= (y_len + 1)
        elif pos_y < 0:
            pos_y += (y_len + 1)

        robots[robot]["position"] = (pos_x, pos_y)

    return robots

def _draw_christmas_tree(robots: Dict[Tuple[int, int], Tuple[int, int]], x_len: int, y_len: int, i: int) -> Any:
    grid = _prepare_grid(x_len, y_len)

    for robot in robots.values():
        x = robot["position"][1]
        y = robot["position"][0]
        grid[x][y] = 255

    im_bytes = bytearray([val for row in grid for val in row])
    im = Image.frombytes(mode="L", size=(x_len, y_len), data=im_bytes)
    im.save(f"{DIR}/chrismtas_tree_{i}.png")

def _prepare_grid(x_len: int, y_len: int) -> List[List[str]]:
    grid = []
    for _ in range(y_len+1):
        grid.append([0 for _ in range(x_len+1)])

    return grid

        
# def main(problem_input: str) -> Any:
#    return
