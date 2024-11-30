from advent_of_code.day4.filippo.solution import (
    main_part_one,
    main_part_two,
    parse_problem_info,
)


def test_number_of_winning_and_owned_numbers_are_parsed_from_string():
    line = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"]
    parsed_info = parse_problem_info(line)
    assert parsed_info[1] == 4


def test_example_part_one():
    problem_input = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    assert main_part_one(problem_input) == 13


def test_example_part_two():
    problem_input = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    assert main_part_two(problem_input) == 30
