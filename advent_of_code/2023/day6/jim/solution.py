import re
import math

def main(problem_input: list[str]):

    pattern = r'\d+'
    times = []
    distances = []
    times = re.findall(pattern, problem_input[0])
    distances = re.findall(pattern, problem_input[1])

    # Part one
    options = []
    for i in range(len(times)):
        options.append(0)
    counter = 0

    for time in times:
        for i in range(0, int(time) + 1):
            dist = (int(time) - i) * i
            if dist > int(distances[counter]):
                options[counter] += 1
        counter += 1        
    
    # Part two
    time_joined = ''.join(times)
    time_joined = int(time_joined)
    distance_joined = ''.join(distances)
    distance_joined = int(distance_joined)
    options2 = 0

    for i in range(0, int(time_joined) + 1):
        dist = (int(time_joined) - i) * i
        if dist > int(distance_joined):
            options2 += 1 

    return math.prod(options), options2 
