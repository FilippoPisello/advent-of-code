"""Solution for day 11 of Advent of Code 2025, by max."""

from typing import Any
from functools import cache


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()

    server_tree = {}
    for line in lines:
        name, seeds = line.split(": ")
        seeds = tuple(seeds.split(" "))
        server_tree[name] = seeds

    paths = [["you"]]
    return len(
        _expand_paths(server_tree, paths, "out", [key for key in server_tree.keys()])
    )


def _expand_paths(
    server_tree: dict, paths: list[list[str]], ending: str, accepted_steps: list[str]
) -> list[list[str]]:
    while True:
        temp_paths = []
        count_outs_and_dead_ends = 0

        for path in paths:
            current_key = path[-1]

            if current_key == ending:
                count_outs_and_dead_ends += 1
                temp_paths.append(path)
                continue

            if current_key in accepted_steps:
                for seed in server_tree[current_key]:
                    temp_path = path.copy()
                    temp_path.append(seed)
                    temp_paths.append(temp_path)

        paths = temp_paths

        if count_outs_and_dead_ends == len(paths):
            break

    return paths


def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    mandatory_nodes = frozenset(["fft", "dac"])

    server_tree = {}
    for line in lines:
        name, seeds = line.split(": ")
        seeds = tuple(seeds.split(" "))
        server_tree[name] = seeds

    @cache
    def count_paths(node: str, visited_mandatory: frozenset) -> int:
        if node in mandatory_nodes:
            visited_mandatory = visited_mandatory | {node}

        if node == "out":
            return 1 if visited_mandatory == mandatory_nodes else 0

        if node not in server_tree:
            return 0

        total = 0
        for child in server_tree[node]:
            total += count_paths(child, visited_mandatory)

        return total

    return count_paths("svr", frozenset())
