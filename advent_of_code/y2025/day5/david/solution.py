"""Solution for day 5 of Advent of Code 2025, by david."""

from typing import Any

# FUCK FILIPPO
def main_part_one(problem_input: str) -> Any:
    fresh_range, ingredients = format_input(problem_input)
    fresh_range_dict = fresh_range_better(fresh_range)
    counter = 0
    for i in ingredients:
        print(i)
        if fresh_range_dict.get(int(i)) is not None:
            counter += 1
    print(counter)
    return


def main_part_two(problem_input: str) -> Any:
    fresh_range, ingredients = format_input(problem_input)
    return


def format_input(input: str) -> Any:
    input_lines = input.splitlines()
    fresh_range = []
    ingredients = []
    for line in input_lines:
        if line == "":
            continue
        elif "-" in line:
            fresh_range.append(line)
        else:
            ingredients.append(line)
    return fresh_range, ingredients


def fresh_range_better(fresh_range: list[str]) -> Any:
    better_ranges = {}
    for fr in fresh_range:
        start, end = fr.split("-")
        for i in range(int(start), int(end) + 1):
            key = i
            better_ranges[key] = True
    return better_ranges


# def main(problem_input: str) -> Any:
#    return
