from advent_of_code.day4.sacha.solution import Card, map_card


def test_map_card():
    test = ["Card   1: 34 55 49| 33 29 "]
    assert map_card(test) == [
        {Card(card_id="Card   1", winning_num=[34, 55, 49], game_num=[33, 29]): 1}
    ]
