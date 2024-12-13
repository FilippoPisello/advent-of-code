"""Solution for day 12 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    garden = parse_data(problem_input)
    # garden_with_fence = add_fences(garden)
    regions = find_regions(garden)
    # fences = find_fences(region)
    return garden


def parse_data(problem_input: str) -> list:
    ls = [list(x) for x in problem_input.split("\n")]
    return ls


def find_regions(garden: list) -> dict:
    regions = {}
    for row, line in enumerate(garden):
        for col, plot in enumerate(line):
            if _is_first_entry(plot, regions):
                # first list is the min row and min col, second list is the max row and max col.
                regions[plot] = [[row, col], [row, col]]
            else:
                regions[plot] = _check_condition(regions, plot, row, col)

    return regions


def find_fences(regions: dict) -> dict:
    fences = {}
    for key, region in regions.items():
        for length in region:
            return


def _is_first_entry(plot: list, regions: dict) -> bool:
    if plot in regions.keys():
        return False
    return True


def _check_condition(region, plot, row, col):
    max_min_loc = region[plot]
    min_row, min_col, max_row, max_col = (
        max_min_loc[0][0],
        max_min_loc[0][1],
        max_min_loc[1][0],
        max_min_loc[0][1],
    )

    if row < min_row:
        min_row = row
    elif row > max_row:
        max_row = row

    if col < min_col:
        min_col = col
    elif col > max_col:
        max_col = col

    return [[min_row, min_col], [max_row, max_col]]


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
