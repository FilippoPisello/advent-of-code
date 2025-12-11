"""Solution for day 10 of Advent of Code 2025, by david."""

from typing import Any
import itertools
import re
from z3 import Int, Optimize


def main_part_one(problem_input: str) -> Any:
    l_indicator_list, buttons_list = format_input_part_one(problem_input)
    buttons_combination = get_all_buttons_combination(buttons_list)
    shortest_path = find_shortest_path(l_indicator_list, buttons_combination)
    return shortest_path


def main_part_two(problem_input: str) -> Any:
    l_indicator_list, buttons_list, joltage_list = format_input_part_two(problem_input)
    for i, joltage in enumerate(joltage_list):
        minimize_problem = use_z3(joltage, buttons_list[i])
    print(joltage_list)
    return


def use_z3(joltage, buttons) -> Any:
    variables = []
    for variable in str(range(len(buttons))):
        variables.append(z3.Real(variable))

    costs = z3.Real("costs")
    opt = z3.Optimize()

    return


def format_input_part_one(input: str) -> Any:
    formated_input = input.strip().split("\n")
    l_indicator_list = []
    buttons_list = []
    for line in formated_input:
        light = re.search(r"\[(.*?)\]", line)
        l_indicator_list.append(light.group(1) if light else "")
        button = re.findall(r"\((.*?)\)", line)
        buttons_list.append(button)
    return l_indicator_list, buttons_list


def format_input_part_two(input: str) -> Any:
    formated_input = input.strip().split("\n")
    l_indicator_list = []
    buttons_list = []
    joltage_levels = []
    for line in formated_input:
        light = re.search(r"\[(.*?)\]", line)
        l_indicator_list.append(light.group(1) if light else "")
        button = re.findall(r"\((.*?)\)", line)
        buttons_list.append(button)
        joltage_level = re.findall(r"\{(.*?)\}", line)
        joltage_levels.append(joltage_level)
    return l_indicator_list, buttons_list, joltage_levels


def get_all_buttons_combination(buttons_list) -> Any:
    buttons_combination = []
    for buttons in buttons_list:
        all_combinations = []
        for r in range(len(buttons) + 1):
            all_combinations.extend(list(itertools.combinations(buttons, r)))
        buttons_combination.append(all_combinations)
    return buttons_combination


def find_shortest_path(l_indicator_list, buttons_combination) -> Any:
    total_shortest_path = 0
    find_shortest_path = 1000
    for i, light in enumerate(l_indicator_list):
        light_int = light.replace("#", "1").replace(".", "0")
        pos = [i for i, x in enumerate(light_int) if x == "1"]
        find_shortest_path = 1000
        for buttons in buttons_combination[i]:
            start_string = "0" * len(light_int)

            for button_str in buttons:
                start_list = list(start_string)
                for pos_str in button_str.split(","):
                    if pos_str.strip():
                        pos = int(pos_str.strip())
                        if 0 <= pos < len(start_list):
                            start_list[pos] = "1" if start_list[pos] == "0" else "0"
                start_string = "".join(start_list)

            if start_string == light_int:
                if len(buttons) < find_shortest_path:
                    find_shortest_path = len(buttons)
        total_shortest_path += find_shortest_path
    return total_shortest_path


# def main(problem_input: str) -> Any:
#    return
