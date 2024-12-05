"""Solution for day 5 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    rules, updates = extract_rules_and_updates(problem_input)
    counter = 0
    for update in updates:
        if _is_valid(update, rules):
            median_index = len(update) // 2
            counter += int(update[median_index])
    return counter


def extract_rules_and_updates(
    problem_input,
) -> tuple[dict[str, set[str]], list[list[str]]]:
    rules, updates = problem_input.split("\n\n")
    rules = _parse_rules(rules)
    updates = [update.split(",") for update in updates.split("\n")]
    return rules, updates


def _parse_rules(rules: str) -> dict[str, set[str]]:
    rules_dict = {}
    for rule in rules.split("\n"):
        value, cannot_be_before = rule.split("|")
        if value in rules_dict:
            rules_dict[value].add(cannot_be_before)
        else:
            rules_dict[value] = {cannot_be_before}
    return rules_dict


def _is_valid(update: list[str], rules: dict[str, set[str]]) -> bool:
    for value, cannot_be_before in rules.items():
        try:
            index_value = update.index(value)
        except ValueError:
            continue
        if any(val in update[:index_value] for val in cannot_be_before):
            return False
    return True


def main_part_two(problem_input: str) -> Any:
    rules, updates = extract_rules_and_updates(problem_input)
    counter = 0
    for update in updates:
        if _is_valid(update, rules):
            continue
        while not _is_valid(update, rules):
            update = _fix_sorting(update, rules)
        median_index = len(update) // 2
        counter += int(update[median_index])
    return counter


def _fix_sorting(update: list[str], rules: dict[str, set[str]]) -> list[str]:
    for value, cannot_be_before in rules.items():
        try:
            index_value = update.index(value)
        except ValueError:
            continue
        for val in cannot_be_before:
            if val not in update[:index_value]:
                continue
            update.remove(val)
            update.insert(index_value, val)
    return update


# def main(problem_input: str) -> Any:
#    return
