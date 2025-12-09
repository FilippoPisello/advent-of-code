"""Solution for day 2 of Advent of Code 2025, by sacha."""

from typing import Any
from math import ceil


def main_part_one(problem_input: str) -> int:
    sum_invalid = 0
    for ids in problem_input.split(','):
        first_id, last_id = map(int, ids.split('-'))
        for id in range(first_id, last_id+1):
            lenght_id = len(str(id))
            if lenght_id % 2 == 0 :
                if str(id)[: lenght_id//2] == str(id)[lenght_id//2 :]:
                    sum_invalid += id
    return sum_invalid

def check_pattern(id:int) -> bool:
    str_id = str(id)
    for i in range(len(str_id)//2):
        div, rst = divmod(len(str_id), i+1)
        if rst == 0:
            if str_id == div*str_id[: i+1]:
                return True
    return False

def main_part_two(problem_input: str) -> int:
    sum_invalid = 0
    for ids in problem_input.split(','):
        first_id, last_id = map(int, ids.split('-'))
        for id in range(first_id, last_id+1):
            if check_pattern(id):
                sum_invalid += id
    return sum_invalid


# def main(problem_input: str) -> Any:
#    return
