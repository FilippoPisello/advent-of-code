"""Solution for day 5 of Advent of Code 2024, by max."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    rules, page_orderings = _parse_problem_input(problem_input)

    safe_orderings = [
        page_ordering
        for page_ordering in page_orderings
        if not any(
            _count_ordering_errors(page, page_ordering, rules) > 0
            for page in page_ordering
        )
    ]

    total = sum(
        int(safe_ordering[len(safe_ordering) // 2]) for safe_ordering in safe_orderings
    )

    return total


def _parse_problem_input(
    problem_input: str,
) -> tuple[list[tuple[str, str]], list[list[str]]]:
    lines = (line for line in problem_input.splitlines() if line)
    rules = []
    page_orderings = []

    for line in lines:
        if len(line) == 5:
            rules.append(tuple(line.split("|")))
        else:
            page_orderings.append(line.split(","))

    return rules, page_orderings


def _count_ordering_errors(
    page: str, page_ordering: list[str], rules: tuple[str, str]
) -> int:
    relevant_rules = [rule[1] for rule in rules if rule[0] == page]

    index_rules = [
        page_ordering.index(rule) for rule in relevant_rules if rule in page_ordering
    ]

    return sum(
        1 for index_rule in index_rules if index_rule < page_ordering.index(page)
    )


def main_part_two(problem_input: str) -> Any:
    rules, page_orderings = _parse_problem_input(problem_input)

    unsafe_orderings = [
        page_ordering
        for page_ordering in page_orderings
        if any(
            _count_ordering_errors(page, page_ordering, rules) > 0
            for page in page_ordering
        )
    ]

    reordered_pages = [
        _reorder_unsafe_ordering(unsafe_ordering, rules)
        for unsafe_ordering in unsafe_orderings
    ]

    total = sum(
        int(reordered_page[len(reordered_page) // 2])
        for reordered_page in reordered_pages
    )

    return total


def _reorder_unsafe_ordering(
    unsafe_ordering: list[str], rules: list[tuple[str, str]]
) -> list[str]:
    while any(
        _count_ordering_errors(page, unsafe_ordering, rules) > 0
        for page in unsafe_ordering
    ):
        for page in unsafe_ordering:
            page_index = unsafe_ordering.index(page)
            relevant_rules = [rule[1] for rule in rules if rule[0] == page]

            for rule in relevant_rules:
                if rule in unsafe_ordering and unsafe_ordering.index(rule) < page_index:
                    unsafe_ordering.remove(rule)
                    unsafe_ordering.insert(page_index, rule)
                    break

    return unsafe_ordering


# def main(problem_input: str) -> Any:
#    return
