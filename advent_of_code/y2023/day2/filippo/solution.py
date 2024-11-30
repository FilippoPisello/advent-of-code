import re
from dataclasses import dataclass
from typing import Self


def main_part_one(problem_input: list[str]):
    total = 0
    for line in problem_input:
        game = Game.from_line(line)
        if game.is_possible(blue=14, red=12, green=13):
            total += game.id
    return total



def main_part_two(problem_input: list[str]):
    total = 0
    for line in problem_input:
        game = Game.from_line(line)
        total += game.cubes
    return total

@dataclass
class Game:
    id: int
    blue: int
    red: int
    green: int

    @classmethod
    def from_line(cls, game_line: str) -> Self:
        constructor = {"blue": 0, "red": 0, "green": 0}
        batches = game_line.split(";")
        for color in constructor.keys():
            for batch in batches:
                new_value = sum([int(x) for x in re.findall(f"(\d*) {color}", batch)])
                if new_value >= constructor[color]:
                    constructor[color] = new_value
        constructor["id"] = int(re.match("Game (\d*)", game_line)[1])
        return cls(**constructor)

    def is_possible(self, blue: int, red: int, green: int) -> bool:
        return (self.blue <= blue) and (self.red <= red) and (self.green <= green)

    @property
    def cubes(self) -> int:
        return self.blue * self.red * self.green