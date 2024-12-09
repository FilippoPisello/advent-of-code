"""Solution for day 9 of Advent of Code 2024, by max."""

from typing import Any, List, Tuple


def main_part_one(problem_input: str) -> Any:
    disk_map = list(map(int, problem_input))
    blocks = _parse_disk_map(disk_map)
    sorted_blocks = _sort_blocks(blocks)

    return sum(block * i for i, block in enumerate(sorted_blocks) if block != ".")


def _parse_disk_map(disk_map: List[int]) -> List[int]:
    output = []
    id = 0

    for i, number in enumerate(disk_map, start=1):
        if i % 2 == 0:
            output.extend(["."] * number)
        else:
            output.extend([id] * number)
            id += 1

    return output


def _sort_blocks(blocks: List[str]) -> List[str]:
    dot_count = blocks.count(".")
    filtered_blocks = [block for block in blocks if block != "."]
    filtered_blocks.sort(reverse=True)

    sorted_blocks = []
    filter_index = 0

    for i in range(len(blocks)):
        if i >= len(blocks) - dot_count:
            sorted_blocks.extend(["."] * (len(blocks) - i))
            break
        elif blocks[i] == ".":
            sorted_blocks.append(filtered_blocks[filter_index])
            filter_index += 1
        else:
            sorted_blocks.append(blocks[i])

    return sorted_blocks


def main_part_two(problem_input: str) -> Any:
    disk_map = list(map(int, problem_input))
    blocks = _parse_disk_map(disk_map)
    sorted_blocks_raw = _sort_whole_blocks(blocks)
    sorted_blocks = []

    for block in sorted_blocks_raw:
        for y in range(block[1]):
            sorted_blocks.append(block[0])

    return sum(block * i for i, block in enumerate(sorted_blocks) if block != ".")


def _sort_whole_blocks(blocks: List[str]) -> List[Tuple[int, int]]:
    blocks_tuple = _group_consecutive_blocks(blocks)

    non_dot_blocks = [block for block in blocks_tuple if block[0] != "."]
    non_dot_blocks.sort(reverse=True)

    for block in non_dot_blocks:
        best_match = _find_best_match(block, blocks_tuple)

        if best_match:
            blocks_tuple.insert(blocks_tuple.index(block), (".", block[1]))
            blocks_tuple.remove(block)
            blocks_tuple.insert(blocks_tuple.index(best_match), block)
            diff = best_match[1] - block[1]
            if diff > 0:
                blocks_tuple.insert(blocks_tuple.index(best_match), (".", diff))
            blocks_tuple.remove(best_match)

    return blocks_tuple


def _find_best_match(
    block: Tuple[str, int], blocks_tuple: List[tuple[str, int]]
) -> Tuple[Tuple[str, int], List[Tuple[str, int]]]:
    matching_blocks = [
        free_block
        for free_block in blocks_tuple
        if free_block[1] >= block[1] and free_block[0] == "."
    ]

    if matching_blocks:
        best_match = matching_blocks[0]
        return best_match

    return


def _group_consecutive_blocks(blocks: List[str]) -> List[Tuple[int, int]]:
    blocks_tuple = []
    current_block = blocks[0]
    current_count = 1

    for block in blocks[1:]:
        if block == current_block:
            current_count += 1
        else:
            blocks_tuple.append((current_block, current_count))
            current_block = block
            current_count = 1

    blocks_tuple.append((current_block, current_count))

    return blocks_tuple


# def main(problem_input: str) -> Any:
#    return
