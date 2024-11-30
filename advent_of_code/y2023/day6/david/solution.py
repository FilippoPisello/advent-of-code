
import re
import math

def main_part_one(problem_input: list[str]):

    
    total = 1
    records = re.findall(r'\d+',problem_input[1])
    race_time = re.findall(r'\d+',problem_input[0])
    number_of_race = len(records)

    for race in range(number_of_race):
        total_possible_win = 0
        # print(int(records[race]))
        for hold_time in range(1,int(race_time[race])):

            race_time_left = int(race_time[race]) - hold_time
            distance = hold_time * race_time_left

            if distance > int(records[race]):
                total_possible_win += 1

        total = total * total_possible_win

    return total



def main_part_two(problem_input: list[str]):

    total = 1
    records = re.findall(r'\d+',problem_input[1].replace(" ",""))
    race_time = re.findall(r'\d+',problem_input[0].replace(" ",""))
    
    # x(time - x) > records
    # - x^2 + x*time - records = 0

    delta = int(race_time[0])*int(race_time[0]) - 4*int(records[0])

    solution1 = (-int(race_time[0])-math.sqrt(delta))/(2*(-1))
    solution2 = (-int(race_time[0])+math.sqrt(delta))/(2*(-1))

    number_of_way_to_win = abs(math.ceil(solution2)-math.ceil(solution1))

    print(number_of_way_to_win)

    
    return total
