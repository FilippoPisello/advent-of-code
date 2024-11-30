import re
import string
from abc import ABC
from dataclasses import dataclass
from typing import ClassVar, Self


def main_part_one(problem_input: list[str]):
    total = 0
    for index, current_row in enumerate(problem_input):
        previous_row = _get_row(index - 1, problem_input)
        next_row = _get_row(index + 1, problem_input)
        numbers = Number.from_line(current_row)
        for number in numbers:
            if (
                has_symbol(current_row, number.same_row_indexes)
                or has_symbol(previous_row, number.adjacent_row_indexes)
                or has_symbol(next_row, number.adjacent_row_indexes)
            ):
                total += number.int_value
    return total


def main_part_two(problem_input: list[str]):
    total = 0
    for index, current_row in enumerate(problem_input):
        previous_row = _get_row(index - 1, problem_input)
        next_row = _get_row(index + 1, problem_input)
        asterisks = Asterisk.from_line(current_row)

        numbers_previous = Number.from_line(previous_row)
        numbers_current = Number.from_line(current_row)
        numbers_next = Number.from_line(next_row)
        for asterisk in asterisks:
            relevant_numbers = (
                get_intersecting_numbers(
                    asterisk.adjacent_row_indexes, numbers_previous
                )
                + get_intersecting_numbers(asterisk.same_row_indexes, numbers_current)
                + get_intersecting_numbers(asterisk.adjacent_row_indexes, numbers_next)
            )
            if len(relevant_numbers) == 2:
                first, second = relevant_numbers
                total += first.int_value * second.int_value
    return total


def _get_row(index: int, problem_input: list[str]) -> str:
    try:
        return problem_input[index]
    except IndexError:
        return "A" * 140


@dataclass
class LineCharacter(ABC):
    value: str
    starting_index: int
    ROW_LENGTH: ClassVar[int] = 140
    REGEX_PATTERN: ClassVar[str] = NotImplementedError

    @property
    def length(self) -> int:
        return len(str(self.value))

    @property
    def ending_index(self) -> int:
        return self.starting_index + self.length - 1

    @property
    def occupied_indexes(self) -> set[int]:
        return {x for x in range(self.starting_index, self.ending_index + 1)}

    @property
    def same_row_indexes(self) -> set[int]:
        if self.starting_index == 0:
            return set([self.ending_index + 1])
        elif self.ending_index == (self.ROW_LENGTH - 1):
            return set([self.starting_index - 1])
        else:
            return set([self.starting_index - 1, self.ending_index + 1])

    @property
    def adjacent_row_indexes(self) -> list[int]:
        return self.same_row_indexes | self.occupied_indexes

    @classmethod
    def from_line(cls, line: str) -> list[Self]:
        expr = re.compile(cls.REGEX_PATTERN)
        return [cls(match.group(), match.span()[0]) for match in expr.finditer(line)]


@dataclass
class Number(LineCharacter):
    REGEX_PATTERN: ClassVar[str] = r"\d+"

    @property
    def int_value(self) -> int:
        return int(self.value)


@dataclass
class Asterisk(LineCharacter):
    REGEX_PATTERN: ClassVar[str] = r"\*"


def extract_asterisks_from_line(line: str) -> list[Asterisk]:
    expr = re.compile(r"\*")
    return [Asterisk(match.group(), match.span()[0]) for match in expr.finditer(line)]


def has_symbol(line: str, indexes: str) -> bool:
    symbols = string.punctuation.replace(".", "")
    for index in indexes:
        if line[index] in symbols:
            return True
    return False


def get_intersecting_numbers(indexes: set[int], numbers: list[Number]) -> list[Number]:
    return [x for x in numbers if x.occupied_indexes & indexes]
