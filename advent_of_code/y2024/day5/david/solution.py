"""Solution for day 5 of Advent of Code 2024, by david."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    puzzle_input = problem_input.split("\n")
    empty = puzzle_input.index("")

    pages_rule = puzzle_input[:empty]
    pages_produce = puzzle_input[empty+1:]

    rules_formatted = []
    produce_formatted = []

    good_updates = []

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
                good_updates.append(update)

    middle_numbers = [int(upd[len(upd)//2]) for upd in good_updates]
    

    return sum(middle_numbers)


def main_part_two(problem_input: str) -> Any:

    puzzle_input = problem_input.split("\n")
    empty = puzzle_input.index("")

    pages_rule = puzzle_input[:empty]
    pages_produce = puzzle_input[empty+1:]

    rules_formatted = []
    produce_formatted = []

    bad_updates = []
    updates_are_now_good = []

    for rule in pages_rule:
        rule_list = rule.split("|")
        rules_formatted.append(rule_list)

    for prod in pages_produce:
        produce_list = prod.split(",")
        produce_formatted.append(produce_list)
    
    for update in produce_formatted:
        if update_is_bad(rules_formatted,update):
            bad_updates.append(update)

    for bad_update in bad_updates:
        update_is_a_baddie_need_to_be_made_a_classic_christian_girl = bad_update
        while update_is_bad(rules_formatted,update_is_a_baddie_need_to_be_made_a_classic_christian_girl):
            to_switch = where_is_it_hurting_doctor(rules_formatted,update_is_a_baddie_need_to_be_made_a_classic_christian_girl)
            update_is_a_baddie_need_to_be_made_a_classic_christian_girl[to_switch[0][0]],update_is_a_baddie_need_to_be_made_a_classic_christian_girl[to_switch[1][0]] = update_is_a_baddie_need_to_be_made_a_classic_christian_girl[to_switch[1][0]],update_is_a_baddie_need_to_be_made_a_classic_christian_girl[to_switch[0][0]]
        updates_are_now_good.append(update_is_a_baddie_need_to_be_made_a_classic_christian_girl)
        middle_numbers = [int(upd[len(upd)//2]) for upd in updates_are_now_good]
    return sum(middle_numbers)

def update_is_bad(rules_list,update):
    for index,page in enumerate(update):
        matching_rules = [lst[0] for lst in rules_list if page in lst[1]]
        issue = [issue_update for issue_update in update[index+1:] if issue_update in matching_rules]
        if issue:
            return True

def where_is_it_hurting_doctor(rules_list,update):
    for index,page in enumerate(update):
        matching_rules = [lst[0] for lst in rules_list if page in lst[1]]
        for bad_index,issue_update in enumerate(update[index + 1:]):
            if issue_update in matching_rules:
                return [[index,page],[index + bad_index + 1,issue_update]]


