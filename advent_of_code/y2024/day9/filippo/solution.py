"""Solution for day 9 of Advent of Code 2024, by filippo."""

from pathlib import Path
from typing import Any

STR_FILE_PATH = Path(__file__).parent / "solution.txt"


def main_part_one(problem_input: str) -> Any:
    problem_input: list[int] = list(map(int, problem_input))
    decoded_str = _decode(problem_input)
    decoded_str = _compact(decoded_str)
    return _compute_checksum(decoded_str)


def _decode(encoded_str: list[int]) -> list[str]:
    decoded_str = []
    odd_chars, even_chars = encoded_str[::2], encoded_str[1::2]
    for index, (odd_char, even_char) in enumerate(zip(odd_chars, even_chars)):
        decoded_str.extend([str(index)] * odd_char)
        decoded_str += "." * even_char
    if len(encoded_str) % 2:
        decoded_str.extend([str(len(even_chars))] * encoded_str[-1])
    return decoded_str


def _compact(decoded_str: list[str]) -> list[str]:
    rightend_index = len(decoded_str) - 1
    for index, char in enumerate(decoded_str):
        if set(decoded_str[index : rightend_index + 1]) == {"."}:
            break
        if char != ".":
            continue
        while (decoded_str[rightend_index] == ".") and (rightend_index > index):
            rightend_index -= 1
            print(rightend_index, end="\r")
        # Swap the two characters
        decoded_str[index], decoded_str[rightend_index] = (
            decoded_str[rightend_index],
            decoded_str[index],
        )

    return decoded_str


def _compute_checksum(decoded_str: list[str]) -> int:
    checksum = 0
    for index, char in enumerate(decoded_str):
        if char == ".":
            break
        checksum += index * int(char)
    return checksum


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
