"""Solution for day 3 of Advent of Code 2024, by david."""

from typing import Any
import re
import numpy as np

def main_part_one(problem_input: str) -> Any:
    program = np.array(re.findall(r"mul\(\d{1,3},\d{1,3}\)",problem_input))
    total = 0
    for mul in program:
        x = re.findall(r"\d{1,3}",mul)
        total += int(x[0])*int(x[1])
    
    return total

def main_part_two(problem_input: str) -> Any:
    program = np.array(re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't|do",problem_input))
    do_or_dont_that_is_the_question = "do"
    total = 0
    for mul in program:
        if mul in ("do","don't"):
            do_or_dont_that_is_the_question = mul
        if do_or_dont_that_is_the_question == "do" and len(mul)>5:
            x = re.findall(r"\d{1,3}",mul)
            total += int(x[0])*int(x[1])
    return total

# def main(problem_input: str) -> Any:
#    return
