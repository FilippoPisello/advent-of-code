"""Solution for day 12 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple
from collections import deque


def main_part_one(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    grid = _make_unique_regions([list(line) for line in inputs])

    garden = {}
    fences = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = grid[row][col]
            count = _evaluate_suroundings(grid, row, col, value)
            
            garden[value] = garden.get(value, 0) + 1
            fences[value] = fences.get(value, 0) + count

    sum = 0
    for type in garden:
        print(f"{type}: {garden[type]}, {fences[type]}")
        sum += garden[type] * fences[type]

    return sum

def _make_unique_regions(grid):

    def is_valid(x, y, char):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == char and (x, y) not in visited

    def flood_fill(x, y, char, replacement):
        queue = deque([(x, y)])
        visited.add((x, y))
        grid[x][y] = replacement

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, char):
                    visited.add((nx, ny))
                    grid[nx][ny] = replacement
                    queue.append((nx, ny))

    visited = set()
    unique_counter = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                char = grid[i][j]
                if char not in unique_counter:
                    unique_counter[char] = 1
                else:
                    unique_counter[char] += 1

                replacement = char if unique_counter[char] == 1 else char + str(unique_counter[char])
                flood_fill(i, j, char, replacement)

    return grid

def _evaluate_suroundings(grid: List[List[str]], row: int, col: int, value: str) -> int:
    neighbors = 0

    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

    for direction in directions:
        x = row + directions[direction][0]
        y = col + directions[direction][1]

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == value:
            neighbors += 1
    options = [4, 3, 2, 1, 0]
    
    return options[neighbors]



def main_part_two(problem_input: str) -> Any:
    inputs = problem_input.splitlines()
    grid = _make_unique_regions([list(line) for line in inputs])

    garden = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = grid[row][col]
            garden[value] = garden.get(value, 0) + 1

    return


# def main(problem_input: str) -> Any:
#    return
