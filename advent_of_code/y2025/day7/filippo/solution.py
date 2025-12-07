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
    problem_input = problem_input.replace("S", "|")

    previous_line = problem_input.splitlines()[0]
    timelines = {previous_line.index("|"): 1}

    for line in problem_input.splitlines()[1:]:
        new_timelines = {}
        for timeline_position, counter in timelines.items():
            new_positions = propagate_timeline(line, timeline_position)
            for new_position in new_positions:
                if new_position in new_timelines:
                    new_timelines[new_position] += counter
                else:
                    new_timelines[new_position] = counter
        timelines = new_timelines

    return sum(timelines.values())


def propagate_timeline(line: str, timeline_position: int) -> list[int]:
    new_positions = []
    if line[timeline_position] == "^":
        if timeline_position > 0:
            new_positions.append(timeline_position - 1)
        if timeline_position < len(line) - 1:
            new_positions.append(timeline_position + 1)
    elif line[timeline_position] == ".":
        new_positions.append(timeline_position)
    return new_positions


# def main(problem_input: str) -> Any:
#    return
