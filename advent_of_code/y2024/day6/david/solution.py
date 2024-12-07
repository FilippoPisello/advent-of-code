"""Solution for day 6 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    puzzle = problem_input.split("\n")
    pos = next([row, line.index("^")] for row, line in enumerate(puzzle) if "^" in line)

    direction = "up"
    all_pos = []
    all_pos.append(pos.copy())

    while is_soldier_not_out(pos, puzzle):
        pos, puzzle, direction = soldier_on_the_move(pos, puzzle, direction)
        all_pos.append(pos.copy())

    tuple_pos = [tuple(sublist) for sublist in all_pos]
    unique_pos = set(tuple_pos)
    unique_count = len(unique_pos)

    return unique_count


def is_soldier_not_out(pos: list[int, int], puzzle: list[str]) -> bool:
    rows = len(puzzle)
    cols = len(puzzle[0])

    if 0 < pos[0] < rows - 1 and 0 < pos[1] < cols - 1:
        return True

    return False


def soldier_on_the_move(pos, puzzle, dir):
    dir_s = {"up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]}
    change_dir = {"up": "right", "right": "down", "down": "left", "left": "up"}

    if puzzle[pos[0] + dir_s[dir][0]][pos[1] + dir_s[dir][1]] == "#":
        dir = change_dir[dir]
        if puzzle[pos[0] + dir_s[dir][0]][pos[1] + dir_s[dir][1]] == "#":
            dir = change_dir[dir]
            if puzzle[pos[0] + dir_s[dir][0]][pos[1] + dir_s[dir][1]] == "#":
                dir = change_dir[dir]
    pos[0] += dir_s[dir][0]
    pos[1] += dir_s[dir][1]
    new_puzzle_string = puzzle[pos[0]][: pos[1]] + "^" + puzzle[pos[0]][pos[1] + 1 :]
    puzzle[pos[0]] = new_puzzle_string

    return pos, puzzle, dir


def main_part_two(problem_input: str) -> Any:
    puzzle = problem_input.split("\n")
    pos = next([row, line.index("^")] for row, line in enumerate(puzzle) if "^" in line)
    total = 0
    direction = "up"
    all_pos = []

    while is_soldier_not_out(pos, puzzle):

        pos_in_loop = pos.copy()
        direction_in_loop = direction
        pos, puzzle, direction = soldier_on_the_move(pos, puzzle, direction)
        puzzle_loop = puzzle.copy()
        puzzle_loop = place_obstacle(puzzle_loop, pos)
        pos_dir = []
        if pos in all_pos:
            print("YOOOOOOOOOO")
        if pos not in all_pos:
            while is_soldier_not_out(pos_in_loop, puzzle_loop):
                pos_in_loop, puzzle_loop, direction_in_loop = soldier_on_the_move(
                    pos_in_loop, puzzle_loop, direction_in_loop
                )
                if is_soldier_in_a_loop(pos_in_loop, direction_in_loop, pos_dir):
                    total += 1
                    print(total)

                    break
                pos_dir.append([pos_in_loop.copy(), direction_in_loop])

        all_pos.append(pos.copy())

    return total


def place_obstacle(puzzle_loop, pos):
    new_puzzle_string = (
        puzzle_loop[pos[0]][: pos[1]] + "#" + puzzle_loop[pos[0]][pos[1] + 1 :]
    )
    puzzle_loop[pos[0]] = new_puzzle_string
    return puzzle_loop


def is_soldier_in_a_loop(pos, dir, pos_dirs):
    for pos_dir in pos_dirs:
        if pos_dir == [pos, dir]:
            return True

    return False


# def main(problem_input: str) -> Any:
#    return
