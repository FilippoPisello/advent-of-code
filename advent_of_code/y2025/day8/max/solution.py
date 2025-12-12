"""Solution for day 8 of Advent of Code 2025, by max."""

from typing import Any, Tuple
import math


def main_part_one(problem_input: str) -> Any:
    # Parameters
    top_pairs = 1000
    top_groups = 3

    # Logic 
    sorted_distances = _get_sorted_distances(problem_input)

    closest_pairs = [pair for pair, _ in sorted_distances[:top_pairs]]

    # Group boxes into sets of closest pairs
    groups = [set(p) for p in closest_pairs]
    changed = True
    while changed:
        changed = False
        new_groups = []

        while groups:
            current = groups.pop(0)

            to_merge = [current]
            remaining = []
            
            for group in groups:
                if current & group:  # If intersection exists
                    to_merge.append(group)
                    changed = True
                else:
                    remaining.append(group)
            
            # Merge all overlapping groups
            merged = set().union(*to_merge)
            new_groups.append(merged)
            groups = remaining

        groups = new_groups
    
    # Get the size of the largest groups
    sizes = sorted([len(group) for group in groups], reverse=True)
    product = 1
    for size in sizes[:top_groups]:
        product *= size
    return product


def _get_eucledian_distance(p: Tuple[int, int, int], q: Tuple[int, int, int]) -> int:
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)


def _get_sorted_distances(problem_input: str) -> list[Tuple[Tuple[int, int], float]]:
    lines = problem_input.splitlines()
    junction_boxes = {}

    for index, line in enumerate(lines):
        line = tuple(map(int, line.split(",")))
        junction_boxes[index] = line
        
    # Get boxes distances from one another
    distances = {}
    indices = list(junction_boxes.keys())

    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            idx_p, idx_q = indices[i], indices[j]
            distance = _get_eucledian_distance(junction_boxes[idx_p], junction_boxes[idx_q])
            distances[(idx_p, idx_q)] = distance

    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    return sorted_distances

def main_part_two(problem_input: str) -> Any:
    # I give up i dont understand.
    return 
