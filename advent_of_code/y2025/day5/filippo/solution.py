"""Solution for day 5 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    ranges, ids = problem_input.split("\n\n")
    int_ranges = [tuple(map(int, line.split("-"))) for line in ranges.splitlines()]
    fresh_count = 0

    for id_ in map(int, ids.splitlines()):
        for start, end in int_ranges:
            if start <= id_ <= end:
                fresh_count += 1
                break

    return fresh_count




def main_part_two(problem_input: str) -> Any:
    ranges, _ = problem_input.split("\n\n")
    int_ranges = [
        (int(line.split("-")[0]), int(line.split("-")[1]))
        for line in ranges.splitlines()
    ]
    ranges_sorted_by_start = sorted(int_ranges, key=lambda r: r[0])
    merged_ranges = extract_unique_ranges(ranges_sorted_by_start)

    assert_ranges_not_overlapping(merged_ranges)

    fresh_count = sum(end - start + 1 for start, end in merged_ranges)
    return fresh_count

def extract_unique_ranges(ranges_sorted_by_start: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged_ranges = []

    while ranges_sorted_by_start:
        current_range = ranges_sorted_by_start.pop(0)
        start_current, end_current = current_range

        indexes_to_remove = []
        for index, other_range in enumerate(ranges_sorted_by_start):
            start_other, end_other = other_range

            # If contained, it is redundant
            if start_current >= start_other and end_other <= end_current:
                indexes_to_remove.append(index)
                continue

            # If overlapping, merge
            if start_other <= end_current:
                end_current = max(end_current, end_other)
                indexes_to_remove.append(index)
                continue

            # If fully outside right, skip
            if end_current < start_other:
                continue

            print(current_range, other_range)
            assert False, "Should not reach here"

        for index in reversed(indexes_to_remove):
            ranges_sorted_by_start.pop(index)

        merged_ranges.append((start_current, end_current))

    return merged_ranges

def assert_ranges_not_overlapping(ranges: list[tuple[int, int]]) -> None:
    for i in range(len(ranges) - 1):
        _, end_current = ranges[i]
        start_next, _ = ranges[i + 1]
        assert end_current < start_next, f"Ranges {ranges[i]} and {ranges[i+1]} are overlapping"

# def main(problem_input: str) -> Any:
#    return
