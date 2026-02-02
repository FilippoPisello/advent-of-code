"""Solution for day 5 of Advent of Code 2025."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    """Solve part one of the puzzle."""
    sections = problem_input.strip().split("\n\n")

    # Parse fresh ingredient ranges
    ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Parse available ingredient IDs
    ingredient_ids = [int(line) for line in sections[1].splitlines()]

    # Count fresh ingredients
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        # Check if ingredient ID falls within any range
        is_fresh = any(start <= ingredient_id <= end for start, end in ranges)
        if is_fresh:
            fresh_count += 1

    return fresh_count


def main_part_two(problem_input: str) -> Any:
    """Solve part two of the puzzle."""
    sections = problem_input.strip().split("\n\n")

    # Parse fresh ingredient ranges (only first section)
    ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Sort ranges by start position
    ranges.sort()

    # Merge overlapping ranges
    merged_ranges = []
    for start, end in ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            # Overlaps or is adjacent to the last merged range
            # Extend the last merged range
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            # No overlap, add as new range
            merged_ranges.append((start, end))

    # Count total ingredient IDs in all merged ranges
    total_count = sum(end - start + 1 for start, end in merged_ranges)

    return total_count
