"""Solution for day 9 of Advent of Code 2024, by filippo."""

import re
from pathlib import Path
from typing import Any

STR_FILE_PATH = Path(__file__).parent / "solution.txt"


def main_part_one(problem_input: str) -> Any:
    decoded_str = _decode(problem_input)
    while _has_fillable_memory(decoded_str):
        decoded_str = _shift_one_memory_unit(decoded_str)
    return _compute_checksum(decoded_str)


def _decode(encoded_str: str) -> str:
    decoded_str = ""
    odd_chars, even_chars = encoded_str[::2], encoded_str[1::2]
    for index, (odd_char, even_char) in enumerate(zip(odd_chars, even_chars)):
        decoded_str += str(index) * int(odd_char)
        decoded_str += "." * int(even_char)
    if len(encoded_str) % 2:
        decoded_str += str(len(even_chars)) * int(encoded_str[-1])
    return decoded_str


def _has_fillable_memory(decoded_str: str) -> bool:
    leftmost_dot_index = decoded_str.find(".")
    # If there are only dots after the leftmost dot, the memory is not fillable
    if set(decoded_str[leftmost_dot_index + 1 :]) == {"."}:
        return False
    return True


def _shift_one_memory_unit(decoded_str: str) -> str:
    leftmost_dot_index = decoded_str.find(".")
    rightmost_digit_index = re.search(r"\d(?=\D*$)", decoded_str).start()
    assert leftmost_dot_index < rightmost_digit_index
    return (
        decoded_str[:leftmost_dot_index]
        + decoded_str[rightmost_digit_index]
        + decoded_str[leftmost_dot_index + 1 : rightmost_digit_index]
        + "."
        + decoded_str[rightmost_digit_index + 1 :]
    )


def _compute_checksum(decoded_str: str) -> int:
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
