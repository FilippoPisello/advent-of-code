"""Solution for day 9 of Advent of Code 2025, by max."""

from collections import defaultdict
from typing import Any, List, Set, Tuple


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()

    largest_rectangle_area = 0

    for i, line in enumerate(lines):
        line = tuple(map(int, line.split(",")))
        remaining_lines = lines[i + 1 :]

        for remaining_line in remaining_lines:
            remaining_line = tuple(map(int, remaining_line.split(",")))

            columns = (
                max(line[0], remaining_line[0]) - min(line[0], remaining_line[0]) + 1
            )
            rows = max(line[1], remaining_line[1]) - min(line[1], remaining_line[1]) + 1

            area = columns * rows
            if area > largest_rectangle_area:
                largest_rectangle_area = area

    return largest_rectangle_area


# Improved logic, by Cursor
def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()

    intervals = _get_complete_rectangle_intervals(lines)

    largest_rectangle_area = 0
    for i, line in enumerate(lines):
        line = tuple(map(int, line.split(",")))
        remaining_lines = lines[i + 1 :]

        for remaining_line in remaining_lines:
            remaining_line = tuple(map(int, remaining_line.split(",")))

            start_column = min(line[0], remaining_line[0])
            end_column = max(line[0], remaining_line[0])
            start_row = min(line[1], remaining_line[1])
            end_row = max(line[1], remaining_line[1])

            # Check if all points in the rectangle are within the filled region
            all_inside = True
            for row in range(start_row, end_row + 1):
                if row not in intervals:
                    all_inside = False
                    break
                min_x, max_x = intervals[row]
                if start_column < min_x or end_column > max_x:
                    all_inside = False
                    break

            if all_inside:
                columns = end_column - start_column + 1
                rows = end_row - start_row + 1
                area = columns * rows
                if area > largest_rectangle_area:
                    largest_rectangle_area = area

    return largest_rectangle_area


def _get_complete_rectangle_intervals(lines: List[str]) -> dict[int, Tuple[int, int]]:
    """Returns a dict mapping row y -> (min_x, max_x) interval for that row."""
    # Parse all points once upfront
    points = [tuple(map(int, line.split(","))) for line in lines]

    # Track min/max x per row directly, no need to store all edge coordinates
    row_bounds: dict[int, list[int]] = defaultdict(list)

    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i + 1 :]:
            if x1 == x2:  # Vertical line - add x to all rows in range
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    row_bounds[y].append(x1)
            if y1 == y2:  # Horizontal line - add x range to this row
                row_bounds[y1].extend([x1, x2])

    # Convert to intervals (min_x, max_x) per row
    intervals: dict[int, Tuple[int, int]] = {}
    for y, x_coords in row_bounds.items():
        intervals[y] = (min(x_coords), max(x_coords))

    return intervals


#   Initial logic, by Max
#   def main_part_two(problem_input: str) -> Any:
#     lines = problem_input.splitlines()

#     complete_rectangle_coordinates = _get_complete_rectangle_coordinates(lines)

#     largest_rectangle_area = 0
#     for i, line in enumerate(lines):
#         line = tuple(map(int, line.split(",")))
#         remaining_lines = lines[i+1:]

#         for remaining_line in remaining_lines:
#             remaining_line = tuple(map(int, remaining_line.split(",")))

#             start_column = min(line[0], remaining_line[0])
#             end_column = max(line[0], remaining_line[0])
#             start_row = min(line[1], remaining_line[1])
#             end_row = max(line[1], remaining_line[1])
#             green_area = 0

#             for column in range(start_column, end_column + 1):
#                 for row in range(start_row, end_row + 1):
#                     if (column, row) in complete_rectangle_coordinates:
#                         green_area += 1
#                         continue
#                     else:
#                         break

#             columns = max(line[0], remaining_line[0]) - min(line[0], remaining_line[0]) + 1
#             rows = max(line[1], remaining_line[1]) - min(line[1], remaining_line[1]) + 1

#             area = columns * rows
#             if green_area == area and area > largest_rectangle_area:
#                 largest_rectangle_area = area

#     return largest_rectangle_area

# def _get_complete_rectangle_coordinates(lines: List[str]) -> List[Tuple[int, int]]:
#     outside_rectangle_coordinates = []
#     for i, line in enumerate(lines):
#         line = tuple(map(int, line.split(",")))
#         remaining_lines = lines[i+1:]

#         for remaining_line in remaining_lines:
#             remaining_line = tuple(map(int, remaining_line.split(",")))

#             if line[0] == remaining_line[0]:
#                 outside_rectangle_coordinates.extend([(line[0], i) for i in range(min(line[1], remaining_line[1]), max(line[1], remaining_line[1]) + 1)])
#             if line[1] == remaining_line[1]:
#                 outside_rectangle_coordinates.extend([(i, line[1]) for i in range(min(line[0], remaining_line[0]), max(line[0], remaining_line[0]) + 1)])

#     unique_outside_rectangle_coordinates = list(set(outside_rectangle_coordinates))

#     complete_rectangle_coordinates = []
#     for row in range(min(unique_outside_rectangle_coordinates, key=lambda x: x[1])[1], max(unique_outside_rectangle_coordinates, key=lambda x: x[1])[1] + 1):
#         filtered_rows = [coordinate for coordinate in unique_outside_rectangle_coordinates if coordinate[1] == row]

#         for column in range(min(filtered_rows, key=lambda x: x[0])[0], max(filtered_rows, key=lambda x: x[0])[0] + 1):
#             complete_rectangle_coordinates.append((column, row))

#     return complete_rectangle_coordinates
