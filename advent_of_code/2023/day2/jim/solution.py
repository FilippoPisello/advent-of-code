import re

red = 12
green = 13
blue = 14

pattern_red = r'(\d+)\s+red'
pattern_green = r'(\d+)\s+green'
pattern_blue = r'(\d+)\s+blue'

def main(problem_input: list[str]):
    
    ##Part One##
    key = 1
    games_dict = {}
    impossible = []
    possible = []
    
    for line in problem_input:
        
        games_dict[key] = line
        key += 1
        
    for key, game in games_dict.items():
        
        r = re.findall(pattern_red, game)
        g = re.findall(pattern_green, game)
        b = re.findall(pattern_blue, game)
        for i in r:
            if int(i) > red:
                impossible.append(key)
        for j in g:
            if int(j) > green:
                impossible.append(key)
        for k in b:
            if int(k) > blue:
                impossible.append(key)

    for i in range (1,101):
        if i not in set(impossible):
            possible.append(i)
    
    ##Part Two##
    total = 0
    
    for key, game in games_dict.items():
        
        r = re.findall(pattern_red, game)
        r = [eval(i) for i in r]
        max_red = max(r)

        g = re.findall(pattern_green, game)
        g = [eval(j) for j in g]
        max_green = max(g)
        
        b = re.findall(pattern_blue, game)
        b = [eval(k) for k in b]
        max_blue = max(b)

        total += max_red * max_green * max_blue
    
    return sum(possible), total

