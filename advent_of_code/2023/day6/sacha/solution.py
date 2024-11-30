from dataclasses import dataclass


@dataclass
class StartMode:
    hold_time: int

    def distance(self, race_time: int) -> int:
        return self.hold_time * (race_time - self.hold_time)


@dataclass
class Race:
    time: int
    record: int

    def is_record(self, new_record: int):
        return self.record < new_record


def main(problem_input: list[str]):
    total = 1
    races = get_races(problem_input)
    for race in races:
        new_record = 0
        counter = 0
        for time in range(race.time):
            distance = StartMode(hold_time=time).distance(race.time)
            if new_record > distance and not race.is_record(distance):
                break
            if race.is_record(distance):
                new_record = distance
                counter += 1
        total = total * counter

    return total


def get_races(problem_input: list[str]) -> list[Race]:
    times = [int(time) for time in problem_input[0].split(":")[1].split()]
    distances = [int(dist) for dist in problem_input[1].split(":")[1].split()]
    races = []
    for time, record in zip(times, distances):
        races.append(Race(time=time, record=record))
    return races
