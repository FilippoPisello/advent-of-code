"""Solution for day 2 of Advent of Code 2025, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:

    input_formatted = [
        list(map(int, part.split("-"))) for part in problem_input.split(",")
    ]
    counter = 0

    for ids in input_formatted:
        for id in range(ids[0], ids[1] + 1):
            id_length = len(str(id))
            if id_length % 2 == 0:
                first_half = str(id)[: id_length // 2]
                second_half = str(id)[id_length // 2 :]
                if first_half == second_half:
                    counter += id

    print(counter)
    return


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
