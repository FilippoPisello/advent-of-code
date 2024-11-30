from advent_of_code.day6.sacha.solution import Race, StartMode, get_races, main

def test_distance():
    mode = StartMode(hold_time=3)
    assert mode.distance(7) == 12

def test_get_race():
    input = ["Time:        58     81","Distance:   434   1041"]
    assert get_races(input) == [Race(time=58,record=434), Race(time=81,record=1041)]

def test_race_beat_record():
    input= ["Time:      7   15   30","Distance:  9   40  200"]
    
    assert main(input)==[4,8,9]
