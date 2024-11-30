from advent_of_code.day3.sacha.solution import (
    mapping_symbol,
    Symbol,
    match_surrounding,
)


def test_mapping_symbol():
    data = ["...*...........197.261", ".....44..&..............."]
    assert mapping_symbol(data) == [
        Symbol(symbol="*", x=3, y=0),
        Symbol(symbol="&", x=9, y=1),
    ]


def test_surrounding():
    test = match_surrounding(2, 4, 1, Symbol(symbol="*", x=3, y=0))
    assert test == True
