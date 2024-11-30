from advent_of_code.day2.filippo.solution import (Game, main_part_one,
                                                  main_part_two)


def test_one_game_is_parsed_to_the_storer_object():
    game_line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert Game.from_line(game_line) == Game(id=1, blue=6, red=4, green=2)


def test_if_multiple_digits_both_are_kept():
    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert Game.from_line(line) == Game(id=3, blue=6, red=20, green=13)


def test_if_one_color_is_missing_max_is_zero():
    game_line = "Game 1: 3 blue, 4 red; 1 red, 6 blue; 2 red"
    actual = Game.from_line(game_line)
    assert actual.green == 0


def test_if_color_appears_twice_in_batch_then_sum():
    game_line = "Game 1: 3 blue, 4 blue; 1 red, 6 blue; 2 red"
    actual = Game.from_line(game_line)
    assert actual.blue == 7


def test_if_id_more_than_two_digits_then_take_all():
    game_line = "Game 78: 3 blue, 4 blue; 1 red, 6 blue; 2 red"
    actual = Game.from_line(game_line)
    assert actual.id == 78


def test_game_is_acceptable_if_all_its_attributes_are_below_provided_values():
    game = Game(id=1, blue=10, red=11, green=12)
    assert game.is_possible(30, 30, 30)


def test_game_is_not_possible_if_one_of_its_attributes_is_above_provided_values():
    game = Game(id=1, blue=100, red=11, green=12)
    assert not game.is_possible(30, 30, 30)


def test_example_part_one():
    example = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert main_part_one(example) == 8

def test_example_part_two():
    example = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert main_part_two(example) == 2286