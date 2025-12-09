"""Solution for day 1 of Advent of Code 2025, by sacha."""

from typing import Any


def main_part_one(problem_input: str) -> int:
    password = 0
    position = 50
    for line in problem_input.splitlines():
        letter, number = line[0], int(line[1:])
        sign = 1 if letter == 'R' else -1
        position = position + sign * number
        password += (position % 100 == 0)
    return password


def main_part_two(problem_input: str) -> int:
    password = 0
    position = 50
    
    for line in problem_input.splitlines():

        letter, number = line[0], int(line[1:])
        sign = 1 if letter == 'R' else -1
        new_position = position + sign * number
        password += abs(new_position) // 100 
        if sign < 0:
            password += (new_position <= 0) - (position == 0)

        position = new_position % 100

    return password


# def main(problem_input: str) -> Any:
#    return
