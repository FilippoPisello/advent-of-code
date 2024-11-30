from dataclasses import dataclass
import re

@dataclass
class Set:
    red: int
    green: int
    blue: int  


def main(problem_input: list[str]):
    bag = Set(12,13,14) #red, green, blue
    succeed_game = 0
    sum_cube = 0
    for game in problem_input:
        helper = {"red": 0, "green":0, "blue":0}
        game_id = get_game_id(game.split(":")[0])
        game_sets = game.split(":")[1].split(';')
        for set in game_sets:
            color_set = get_colors(set)
            helper["red"]=max(helper["red"], color_set.red)
            helper["green"]=max(helper["green"], color_set.green)
            helper["blue"]=max(helper["blue"], color_set.blue)
        if helper["red"] <= bag.red and helper["blue"] <= bag.blue and helper["green"] <= bag.green:
            succeed_game += game_id
        sum_cube += helper["red"]*helper["green"]*helper["blue"]
    return succeed_game, sum_cube

def get_game_id(game):
    id = int(game.split()[1].rstrip(':'))
    return id

def get_colors(set):
    red = sum([int(x) for x in re.findall(r'(\d+)\s+red', set)])
    green = sum([int(x) for x in re.findall(r'(\d+)\s+green', set)])
    blue = sum([int(x) for x in re.findall(r'(\d+)\s+blue', set)])
    return Set(red=red,green=green,blue=blue)


