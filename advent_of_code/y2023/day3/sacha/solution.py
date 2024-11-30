from dataclasses import dataclass
import re
from collections import defaultdict
from math import prod


@dataclass
class Symbol:
    symbol: str
    x: int
    y: int


def main(problem_input: list[str]):
    map_symbol = mapping_symbol(problem_input)
    gear_match = defaultdict(list)
    digits = []
    for line_num, line in enumerate(problem_input):
        for match in re.finditer(r"\d+", line):
            for symbol in map_symbol:
                if match_surrounding(match.start(), match.end(), line_num, symbol):
                    digits.append(int(match.group()))
                    if symbol.symbol == "*":
                        gear_match[(symbol.x, symbol.y)].append(int(match.group()))
    return sum(digits), sum(
        prod(gear) for gear in gear_match.values() if len(gear) == 2
    )


def mapping_symbol(problem_input: list[str]) -> list[Symbol]:
    map_symbol = []
    for y in range(len(problem_input)):
        for x in range(len(problem_input[0])):
            if problem_input[y][x] not in "01234566789.":
                map_symbol.append(Symbol(symbol=problem_input[y][x], x=x, y=y))
    return map_symbol


def match_surrounding(match_start: int, match_end: int, line_num: int, symbol: Symbol):
    return (
        symbol.x <= (match_end)
        and symbol.x >= (match_start - 1)
        and symbol.y >= line_num - 1
        and symbol.y <= line_num + 1
    )
