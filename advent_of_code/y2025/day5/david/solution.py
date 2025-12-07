"""Solution for day 5 of Advent of Code 2025, by david."""

from tracemalloc import start
from typing import Any


def main_part_one(problem_input: str) -> Any:
    fresh_range, ingredients = format_input(problem_input)
    counter = 0
    for i in ingredients:
        for fr in fresh_range:
            start, end = fr.split("-")
            if int(i) >= int(start) and int(i) <= int(end):
                counter += 1
                break
    return counter


def main_part_two(problem_input: str) -> Any:
    fresh_range, ingredients = format_input(problem_input)
    fresh_range_part_two = [list(map(int, fr.split("-"))) for fr in fresh_range]
    fresh_range_part_two = sorted(fresh_range_part_two, key=lambda x: x[0])
    final_ranges = []
    counter = 0

    while fresh_range_part_two:
        first_element = fresh_range_part_two.pop(0)
        current_start = first_element[0]
        current_end = first_element[1]
        index_to_remove = []

        for index, other in enumerate(fresh_range_part_two):
            other_start = other[0]
            other_end = other[1]

            if other_start <= current_end:
                current_end = max(current_end, other_end)
                index_to_remove.append(index)
            elif other_start > current_end:
                break

        final_ranges.append([current_start, current_end])
        index_to_remove.sort(reverse=True)
        for index in index_to_remove:
            fresh_range_part_two.pop(index)

    for final in final_ranges:
        counter += 1 + final[1] - final[0]
    return counter


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


# def main(problem_input: str) -> Any:
#    return
