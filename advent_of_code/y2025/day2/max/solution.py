"""Solution for day 2 of Advent of Code 2025, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    product_ids = _get_product_ids(problem_input)

    # Check if product ids are valid
    product_ids_invalid = []
    for product_id in product_ids:
        if len(str(product_id)) % 2 == 0:
            first_half = str(product_id)[: len(str(product_id)) // 2]
            second_half = str(product_id)[len(str(product_id)) // 2 :]
            if first_half == second_half:
                product_ids_invalid.append(product_id)

    return sum(product_ids_invalid)


def main_part_two(problem_input: str) -> Any:
    product_ids = _get_product_ids(problem_input)

    # Check if product ids are valid
    product_ids_invalid = []
    for product_id in product_ids:
        for split in range(1, len(str(product_id)) // 2 + 1):
            splits = set(
                [
                    str(product_id)[i : i + split]
                    for i in range(0, len(str(product_id)), split)
                ]
            )
            if len(splits) == 1:
                product_ids_invalid.append(product_id)
                break

    return sum(product_ids_invalid)


def _get_product_ids(problem_input: str) -> list[int]:
    ranges_input = problem_input.split(",")
    product_ids = []

    for range_input in ranges_input:
        range_start, range_end = range_input.split("-")
        for i in range(int(range_start), int(range_end) + 1):
            product_ids.append(i)

    return product_ids
