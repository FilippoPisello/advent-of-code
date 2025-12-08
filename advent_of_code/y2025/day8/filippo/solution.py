"""Solution for day 8 of Advent of Code 2025, by filippo."""

from typing import Any

Box = tuple[int, int, int]


def main_part_one(problem_input: str, n_connections: int = 1000) -> Any:
    boxes = parse_boxes(problem_input)

    distance_matrix = compute_distances(list(boxes.keys()))
    sorted_distance_pairs = sorted(
        distance_matrix.keys(), key=lambda item: distance_matrix[item]
    )
    connected_boxes = form_connections(boxes, sorted_distance_pairs, n_connections)

    count_by_group_id = count_groups(connected_boxes)

    sorted_counts = sorted(count_by_group_id.values(), reverse=True)
    sorted_counts += [1] * (3 - len(sorted_counts))  # Ensure at least 3 counts
    return sorted_counts[0] * sorted_counts[1] * sorted_counts[2]


def parse_boxes(problem_input: str) -> dict[Box, int | None]:
    return {
        tuple(map(int, line.split(","))): None for line in problem_input.splitlines()  # type: ignore
    }


def compute_distances(boxes: list[Box]) -> dict[tuple[Box, Box], float]:
    distances = {}
    for i, box1 in enumerate(boxes):
        for box2 in boxes[i + 1 :]:
            distance = (
                (box1[0] - box2[0]) ** 2
                + (box1[1] - box2[1]) ** 2
                + (box1[2] - box2[2]) ** 2
            ) ** 0.5
            distances[(box1, box2)] = distance
    return distances


def form_connections(
    boxes: dict[Box, int | None],
    sorted_distance_pairs: list[tuple[Box, Box]],
    n_connections: int,
) -> dict[Box, int | None]:
    connected_boxes = boxes.copy()

    group_id = 0
    for box1, box2 in sorted_distance_pairs[:n_connections]:
        if connected_boxes[box1] is None and connected_boxes[box2] is None:
            connected_boxes[box1] = group_id
            connected_boxes[box2] = group_id
            group_id += 1
        elif connected_boxes[box1] is not None and connected_boxes[box2] is None:
            connected_boxes[box2] = connected_boxes[box1]
        elif connected_boxes[box1] is None and connected_boxes[box2] is not None:
            connected_boxes[box1] = connected_boxes[box2]
        # If both boxes are already connected, merge them and keep lowest group id
        elif connected_boxes[box1] != connected_boxes[box2]:
            id_to_keep = min(connected_boxes[box1], connected_boxes[box2])
            id_to_update = max(connected_boxes[box1], connected_boxes[box2])
            for box in connected_boxes:
                if connected_boxes[box] == id_to_update:
                    connected_boxes[box] = id_to_keep

    return connected_boxes


def count_groups(connected_boxes: dict[Box, int | None]) -> dict[int, int]:
    count_by_group_id = {}
    for group_id in set(connected_boxes.values()):
        if group_id is not None:
            count_by_group_id[group_id] = sum(
                1 for box in connected_boxes if connected_boxes[box] == group_id
            )
    return {
        k: v
        for k, v in sorted(
            count_by_group_id.items(), key=lambda item: item[1], reverse=True
        )
    }


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
