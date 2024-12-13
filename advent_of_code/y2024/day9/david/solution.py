"""Solution for day 9 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    string_list = [list(x) for x in problem_input.split()]
    disk_map = string_list[0]

    disk_map_1_step = first_step(disk_map)
    chars_nbr = len(disk_map_1_step)
    for index, file_block in enumerate(disk_map_1_step):
        print(index)
        if all(x == -1 for x in disk_map_1_step[index:]):
            break
        if file_block == -1:
            reverse_map = disk_map_1_step[::-1]
            for reverse_index, file_reverse_block in enumerate(reverse_map):
                if file_reverse_block != -1:
                    disk_map_1_step[index] = file_reverse_block
                    disk_map_1_step[chars_nbr - 1 - reverse_index] = -1
                    break

    total = 0
    for x, y in enumerate(disk_map_1_step):
        if y > 0:
            total += x * y

    return total


def first_step(disk_map):
    disk_map_1_step = []
    for index, file in enumerate(disk_map):
        if index % 2 == 0:
            for _ in range(int(file)):
                disk_map_1_step.append(round(index / 2))
        else:
            for _ in range(int(file)):
                disk_map_1_step.append(-1)
    return disk_map_1_step


def main_part_two(problem_input: str) -> Any:

    string_list = [list(x) for x in problem_input.split()]
    disk_map = string_list[0]
    disk_map = first_step(disk_map)
    chars_nbr = len(disk_map)
    for index, file_block in enumerate(disk_map):
        print(index)
        if all(x == -1 for x in disk_map[index:]):
            break
        if file_block == -1:
            reverse_map = disk_map[::-1]
            for reverse_index, file_reverse_block in enumerate(reverse_map):
                if file_reverse_block != -1:
                    disk_map[index] = file_reverse_block
                    disk_map[chars_nbr - 1 - reverse_index] = -1
                    break

    total = 0
    for x, y in enumerate(disk_map):
        if y > 0:
            total += x * y

    return total


# def main(problem_input: str) -> Any:
#    return
