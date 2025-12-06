"""Solution for day 5 of Advent of Code 2025, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    fresh_ingredients_ranges, available_ingredients = problem_input.split("\n\n")

    fresh_ingredients_dict = {}
    for index, fresh_ingredient_range in enumerate[str](
        fresh_ingredients_ranges.splitlines()
    ):
        start, end = map(int, fresh_ingredient_range.split("-"))
        fresh_ingredients_dict[index] = {
            "start": start,
            "end": end,
        }

    fresh_ingredients_count = 0
    for ingredient_id in available_ingredients.splitlines():
        for fresh_ingredient_range in fresh_ingredients_dict.values():
            if (
                fresh_ingredient_range["start"]
                <= int(ingredient_id)
                <= fresh_ingredient_range["end"]
            ):
                fresh_ingredients_count += 1
                break

    return fresh_ingredients_count


def main_part_two(problem_input: str) -> Any:
    fresh_ingredients_ranges, available_ingredients = problem_input.split("\n\n")

    fresh_ingredients = []
    for fresh_ingredient_range in fresh_ingredients_ranges.splitlines():
        start, end = map(int, fresh_ingredient_range.split("-"))
        fresh_ingredients.append((start, end))

    fresh_ingredients_sorted = sorted(fresh_ingredients, key=lambda x: x[0])

    merged_fresh_ingredients = []
    while fresh_ingredients_sorted:
        start, end = fresh_ingredients_sorted.pop(0)
        index_to_remove = []

        for index, other_fresh_ingredient in enumerate(fresh_ingredients_sorted):
            other_start, other_end = other_fresh_ingredient

            # overlapping: extend
            if other_start <= end:
                end = max(end, other_end)
                index_to_remove.append(index)

            # its own thing
            if other_start > end:
                continue

        for index in reversed(index_to_remove):
            fresh_ingredients_sorted.pop(index)

        merged_fresh_ingredients.append((start, end))

    fresh_ingredients_count = 0
    for start, end in merged_fresh_ingredients:
        fresh_ingredients_count += end - start + 1

    return fresh_ingredients_count


# def main(problem_input: str) -> Any:
#    return
# 338258295736104
