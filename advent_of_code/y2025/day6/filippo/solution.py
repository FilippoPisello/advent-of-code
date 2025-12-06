"""Solution for day 6 of Advent of Code 2025, by filippo."""

from typing import Any
from unicodedata import digit


def main_part_one(problem_input: str) -> Any:
    total = 0
    values: dict[int, list[int]] = {}
    for row in problem_input.splitlines():
        for index, value in enumerate(row.split()):
            if value.isdigit():
                if index not in values:
                    values[index] = []
                values[index].append(int(value))
            else:
                if value == "+":
                    total += sum(values[index])
                elif value == "*":
                    prod = 1
                    for v in values[index]:
                        prod *= v
                    total += prod
    return total


def main_part_two(problem_input: str) -> Any:
    values: dict[int, list[int]] = {}
    problems = []

    split_value_columns(problem_input)

    return sum(problems)


def split_value_columns(problem_input: str) -> list[list[str]]:
    lines = problem_input.splitlines()
    signs_line = lines[-1]
    starting_index = 0
    raw_value_columns: list[list[str]] = []
    for index, character in enumerate(signs_line[1:], start=1):
        is_last_character = index == len(signs_line) - 1
        if (character != " ") or is_last_character:
            segment_start = starting_index
            if is_last_character:
                segment_end = index + 1
            else:
                segment_end = index - 1
            extracted_col = [line[segment_start:segment_end] for line in lines[:-1]]
            print(extracted_col)
            raw_value_columns.append(extracted_col)
            starting_index = index
    return raw_value_columns


def recode_values(raw_values: list[int]) -> list[int]:
    destructured_values: list[dict[int, str]] = []
    max_index = 0

    for value in raw_values:
        index_map = {}

        for index, digit in enumerate(str(value)):
            index_map[index] = digit
            if index > max_index:
                max_index = index
        destructured_values.append(index_map)

    recoded_values: list[int] = []
    for index in range(max_index + 1):
        recoded_value_str = ""
        for value_map in destructured_values:
            if index in value_map:
                recoded_value_str += value_map[index]
        recoded_values.append(int(recoded_value_str))

    return recoded_values
