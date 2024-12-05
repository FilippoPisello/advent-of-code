"""Solution for day 5 of Advent of Code 2024, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    rules, updates = problem_input.split("\n\n")
    rules = _parse_rules(rules)
    updates = [update.split(",") for update in updates.split("\n")]
    counter = 0
    for update in updates:
        if _is_valid(update, rules):
            median_index = len(update) // 2
            counter += int(update[median_index])
    return counter


def _parse_rules(rules: str) -> dict[str, set[str]]:
    rules_dict = {}
    for rule in rules.split("\n"):
        before, after = rule.split("|")
        if rule in rules_dict:
            rules_dict[before].add(after)
        else:
            rules_dict[before] = {after}
    return rules_dict


def _is_valid(update: list[str], rules: dict[str, set[str]]) -> bool:
    for before, after in rules.items():
        try:
            index_before = update.index(before)
        except ValueError:
            continue
        if any(val in update[:index_before] for val in after):
            return False
    return True


def main_part_two(problem_input: str) -> Any:
    return


# def main(problem_input: str) -> Any:
#    return
