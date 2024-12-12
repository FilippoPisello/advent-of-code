"""Solution for day 11 of Advent of Code 2024, by max."""

from typing import Any


def main_part_one(problem_input: str) -> int:
    return _blink(problem_input, 25)


def _blink(problem_input: str, blinks: int) -> int:
    stones = {}
    for stone in map(int, problem_input.split()):
        stones[stone] = stones.get(stone, 0) + 1

    for _ in range(blinks):
        print(_)
        new_stones = {}

        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + count
                continue

            stone_str = str(stone)

            if len(stone_str) > 1 and len(stone_str) % 2 == 0 and stone_str.isdigit():
                mid = len(stone_str) // 2
                left_half = int(stone_str[:mid])
                right_half = int(stone_str[mid:])

                new_stones[left_half] = new_stones.get(left_half, 0) + count
                new_stones[right_half] = new_stones.get(right_half, 0) + count
            else:
                large_stone = stone * 2024
                new_stones[large_stone] = new_stones.get(large_stone, 0) + count

        stones = new_stones

    return sum(stones.values())


def main_part_two(problem_input: str) -> int:
    return _blink(problem_input, 75)


# def main(problem_input: str) -> Any:
#    return
