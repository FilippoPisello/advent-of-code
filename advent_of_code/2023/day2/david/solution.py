import os
import re

def main_part_one(problem_input: list[str]):
    max_red = 12
    max_green = 13
    max_blue = 14

    counter = 0
    total = 0


    for i in problem_input:
        counter += 1
        result = i.split(';')
        false = 0

        pattern_green = r'(\d+)\s+green'
        pattern_red = r'(\d+)\s+red'
        pattern_blue = r'(\d+)\s+blue'

        for j in result:
            match_green = re.search(pattern_green, j)
            if match_green:
                if int(match_green.group(1)) > max_green:
                    false = -1
                    break
            
            match_red = re.search(pattern_red, j)
            if match_red:
                if int(match_red.group(1)) > max_red:
                    false = -1
                    break
            
            match_blue = re.search(pattern_blue, j)
            if match_blue:
                if int(match_blue.group(1)) > max_blue:
                    false = -1
                    break
        if(false != -1):
            total += counter

    return total


def main_part_two(problem_input: list[str]):


    counter = 0
    total = 0

    for i in problem_input:
        counter += 1
        result = i.split(';')
        false = 0

        pattern_green = r'(\d+)\s+green'
        pattern_red = r'(\d+)\s+red'
        pattern_blue = r'(\d+)\s+blue'

        max_green = 0
        max_red = 0
        max_blue = 0
        for j in result:
            match_green = re.search(pattern_green, j)

            if match_green:
                if int(match_green.group(1)):
                    if int(match_green.group(1)) > max_green:
                        max_green = int(match_green.group(1))
            

            match_red = re.search(pattern_red, j)
            if match_red:
                if int(match_red.group(1)):
                    if int(match_red.group(1)) > max_red:
                        max_red = int(match_red.group(1))
            
            match_blue = re.search(pattern_blue, j)
            if match_blue:
                if int(match_blue.group(1)):
                    if int(match_blue.group(1)) > max_blue:
                        max_blue = int(match_blue.group(1))


        total += max_blue * max_red * max_green
    
    return total