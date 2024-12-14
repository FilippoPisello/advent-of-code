"""Solution for day 11 of Advent of Code 2024, by filippo."""

from functools import partial
from typing import Any


def main(problem_input: str, iterations: int) -> Any:
    stones = [int(x) for x in problem_input.split(" ")]
    counter = {}
    _add_stones_to_counter(stones, counter)
    for n in range(iterations):
        print(n, end="\r", flush=True)
        new_counter = {}
        for stone, count in counter.items():
            new_stones = _blink(stone)
            for stone in new_stones:
                if stone not in new_counter:
                    new_counter[stone] = 0
                new_counter[stone] += count
        counter = new_counter
    return sum(counter.values())


def _add_stones_to_counter(stones: list[int], counter: dict[int, int]) -> None:
    for stone in stones:
        if stone not in counter:
            counter[stone] = 1
        else:
            counter[stone] += 1


def _blink(n: int) -> list[int]:
    if n == 0:
        return [1]
    str_int = str(n)
    len_str_int = len(str_int)
    if not (len_str_int % 2):
        return [int(str_int[: len_str_int // 2]), int(str_int[len_str_int // 2 :])]
    return [2024 * n]


main_part_one = partial(main, iterations=25)
main_part_two = partial(main, iterations=75)
