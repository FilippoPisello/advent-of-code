"""Solution for day 7 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    problem_input = problem_input.replace("S", "|")

    tot_split_count = 0
    previous_line = problem_input.splitlines()[0]
    for line in problem_input.splitlines()[1:]:
        transformed_line, split_count = propagate_ray(line, previous_line)
        previous_line = transformed_line
        tot_split_count += split_count

    return tot_split_count


def propagate_ray(line: str, previous_line: str) -> tuple[str, int]:
    split_count = 0
    transformed_line = ["." for _ in line]
    for index, char in enumerate(line):
        if previous_line[index] == "|":
            transformed_line[index] = "|"

        if char == "^":
            transformed_line[index] = "^"
            if previous_line[index] == "|":
                split_count += 1
                transformed_line[index - 1] = "|"
                transformed_line[index + 1] = "|"

    return "".join(transformed_line), split_count


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
