from dataclasses import dataclass
from math import ceil, floor, sqrt


def main_part_one(problem_input: list[str]):
    races = parse_races_from_lines(problem_input)
    output = 1
    for race in races:
        output = output * race.winning_options()
    return output


def main_part_two(problem_input: list[str]):
    race = parse_race_as_one(problem_input)
    return race.winning_options()


@dataclass
class Race:
    time: int
    record_distance: int

    def winning_options(self) -> int:
        """This is equivalent to solving the grade 2 inequality:
        waiting_time^2 - time * waiting_time > record_distance

        Which is derived from the equation:
        distance = speed * (time - waiting_time)
        speed = waiting_time

        Only caveat is that we only need to get the acceptable integer values.
        """
        delta = self.time**2 - 4 * self.record_distance
        _max = (self.time + sqrt(delta)) / 2
        _min = (self.time - sqrt(delta)) / 2
        return floor(_max - 0.01) - ceil(_min + 0.01) + 1


def parse_races_from_lines(lines: list[str]) -> list[Race]:
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    return [
        Race(time=int(time), record_distance=int(distance))
        for time, distance in zip(times, distances)
    ]


def parse_race_as_one(lines: list[str]) -> Race:
    times = "".join(lines[0].split()[1:])
    distances = "".join(lines[1].split()[1:])
    return Race(time=int(times), record_distance=int(distances))
