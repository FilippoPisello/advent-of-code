from advent_of_code.day2.sacha.solution import main, get_game_id, get_colors, Set

def test_get_id():
    game = "Game 3: 2 blue, 3 red; 3 green, 3 blue, 6 red; 4 blue, 6 red; 2 green, 2 blue, 9 red; 2 red, 4 blue"
    test_id = get_game_id(game.split(":")[0])
    assert test_id == 3

def test_get_color():
    set = ' 2 blue, 3 red'
    test = get_colors(set)
    assert test == Set(3,0,2)

def test_good_game():
    game = ["Game 1: 2 blue, 3 red; 3 green, 3 blue, 6 red; 4 blue, 6 red; 2 green, 2 blue, 9 red; 2 red, 4 blue"]
    test = main(game)
    assert test == (1,108)

def test_bad_game():
    game = ["Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"]
    test = main(game)
    assert test == (0,1560)
