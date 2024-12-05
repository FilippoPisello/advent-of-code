"""Solution for day 5 of Advent of Code 2024, by david."""

from typing import Any
import re


def main_part_one(problem_input: str) -> Any:
    puzzle_input = problem_input.split("\n")
    empty = puzzle_input.index("")

    pages_rule = puzzle_input[:empty]
    pages_produce = puzzle_input[empty+1:]

    rules_formatted = []
    produce_formatted = []

    good_update = []

    for rule in pages_rule:
        rule_list = rule.split("|")
        rules_formatted.append(rule_list)

    for prod in pages_produce:
        produce_list = prod.split(",")
        produce_formatted.append(produce_list)
    
    for update in produce_formatted:
        for index,page in enumerate(update):
            matching_rules = [lst[0] for lst in rules_formatted if page in lst[1]]
            issue = [issue_update for issue_update in update[index+1:] if issue_update in matching_rules]

            if issue:
                break
            
            if index == len(update)-1:
                good_update.append(update)

    middle_numbers = [int(upd[len(upd)//2]) for upd in good_update]
    

    return sum(middle_numbers)


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
