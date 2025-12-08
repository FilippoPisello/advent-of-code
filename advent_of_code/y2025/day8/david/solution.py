"""Solution for day 8 of Advent of Code 2025, by david."""

from cmath import sqrt
from math import prod
from typing import Any


def main_part_one(problem_input: str) -> Any:

    boxes_dict = create_boxes_dict(problem_input)
    dist_boxes_grid = calculate_distances(boxes_dict)
    clostest_n_pair = connect_closest_pair_faster(dist_boxes_grid, 1000)
    circuit = create_circuit(clostest_n_pair)
    top_3_lengths = sorted([len(c) for c in circuit], reverse=True)[:3]
    return prod(top_3_lengths)


def main_part_two(problem_input: str) -> Any:
    boxes_dict = create_boxes_dict(problem_input)
    dist_boxes_grid = calculate_distances(boxes_dict)
    last_two_pair = connect_closest_pair_faster_and_one_circuit(dist_boxes_grid)

    return boxes_dict[last_two_pair[0]][0] * boxes_dict[last_two_pair[1]][0]


def create_boxes_dict(input: str) -> dict:
    boxes_dict = {}
    input_lines = input.splitlines()
    counter = 0
    for line in input_lines:
        boxes_dict[counter] = list(map(int, line.split(",")))
        counter += 1
    return boxes_dict


def calculate_distances(boxes_dict: dict) -> list:
    dist_boxes_grid = [
        [0 for _ in range(len(boxes_dict))] for _ in range(len(boxes_dict))
    ]
    for box_id, box in boxes_dict.items():
        for other_box_id, other_box in boxes_dict.items():
            if box_id == other_box_id:
                continue
            else:
                dist_boxes_grid[box_id][other_box_id] = sqrt(
                    pow((box[0] - other_box[0]), 2)
                    + pow((box[1] - other_box[1]), 2)
                    + pow((box[2] - other_box[2]), 2)
                ).real
    return dist_boxes_grid


def connect_closest_pair(dist_boxes_grid: list, n: int) -> list:
    l = []
    counter = 0
    min_indices = (0, 0)
    while counter < n:
        min_value = float("inf")
        for i, row in enumerate(dist_boxes_grid):
            for j, value in enumerate(row):
                if value > 0 and value < min_value:
                    min_value = value
                    min_indices = [i, j]
        l.append(min_indices)
        dist_boxes_grid[min_indices[0]][min_indices[1]] = float("inf")
        dist_boxes_grid[min_indices[1]][min_indices[0]] = float("inf")
        counter += 1
    return l


def connect_closest_pair_faster(dist_boxes_grid: list, n: int) -> list:
    r = len(dist_boxes_grid)
    all_edges = []

    for i in range(r):
        for j in range(i + 1, r):
            distance = dist_boxes_grid[i][j]
            if distance > 0:
                all_edges.append((distance, i, j))

    all_edges.sort()

    result_indices = [[i, j] for distance, i, j in all_edges[:n]]

    return result_indices


def connect_closest_pair_faster_and_one_circuit(dist_boxes_grid: list) -> list:
    r = len(dist_boxes_grid)
    all_edges = []

    for i in range(r):
        for j in range(i + 1, r):
            distance = dist_boxes_grid[i][j]
            if distance > 0:
                all_edges.append((distance, i, j))

    all_edges.sort()
    circuits = []

    for distance, i, j in all_edges:
        circuits = add_to_circuits(circuits, [i, j])
        if len(circuits) == 1 and len(circuits[0]) == r:
            return [i, j]

    return circuits


def create_circuit(closest_n_pair: list) -> Any:
    circuits = []
    for current_row in closest_n_pair:
        current_set = set(current_row)

        circuits_to_merge_indices = []
        for i, existing_circuit in enumerate(circuits):
            existing_set = set(existing_circuit)
            if current_set.intersection(existing_set):
                circuits_to_merge_indices.append(i)

        if not circuits_to_merge_indices:
            circuits.append(current_row)

        else:
            target_id = circuits_to_merge_indices[0]
            merged_set = set(circuits[target_id])
            merged_set.update(current_set)

            for merge_id in circuits_to_merge_indices[1:]:
                merged_set.update(circuits[merge_id])

            circuits[target_id] = list(merged_set)
            for i in sorted(circuits_to_merge_indices[1:], reverse=True):
                del circuits[i]

    return circuits


def add_to_circuits(circuits: list, pair: list) -> list:
    current_set = set(pair)

    circuits_to_merge_indices = []
    for i, existing_circuit in enumerate(circuits):
        existing_set = set(existing_circuit)
        if current_set.intersection(existing_set):
            circuits_to_merge_indices.append(i)

    if not circuits_to_merge_indices:
        circuits.append(pair)

    else:
        target_id = circuits_to_merge_indices[0]
        merged_set = set(circuits[target_id])
        merged_set.update(current_set)

        for merge_id in circuits_to_merge_indices[1:]:
            merged_set.update(circuits[merge_id])

        circuits[target_id] = list(merged_set)
        for i in sorted(circuits_to_merge_indices[1:], reverse=True):
            del circuits[i]

    return circuits


# def main(problem_input: str) -> Any:
#    return
