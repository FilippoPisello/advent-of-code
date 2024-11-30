from collections import defaultdict
import re


def main(problem_input: list[str]):
    dict, instruction = input_to_dict(problem_input)
    step = dict["AAA"]
    counter = 0
    while True:
        for i in range(len(instruction)):
            next_step = step[int(instruction[i])]
            step = dict[next_step]
            counter += 1
            if next_step == "ZZZ":
                break
        else:
            continue
        break
    return counter


def input_to_dict(
    problem_input: list[str],
) -> tuple(dict[str, list],):
    instruction = problem_input[0].replace("L", "0").replace("R", "1")
    mapping = problem_input[2:]
    dict = defaultdict(list)
    for line in mapping:
        matches = re.findall(r"\b\w+\b", line)
        dict.update({matches[0]: matches[1:]})
    return dict, instruction
