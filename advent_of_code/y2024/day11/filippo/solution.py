"""Solution for day 11 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    stones = [int(x) for x in problem_input.split(" ")]
    for _ in range(25):
        new_stones = []
        for stone in stones:
            for res in _blink(stone):
                new_stones.append(res)
        stones = new_stones
    return len(stones)


def _blink(n: int) -> list[int]:
    if n == 0:
        return [1]
    str_int = str(n)
    len_str_int = len(str_int)
    if not (len_str_int % 2):
        return [int(str_int[: len_str_int // 2]), int(str_int[len_str_int // 2 :])]
    return [2024 * n]


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
