import os
import re

module_path = os.path.dirname(os.path.abspath(__file__))
python_path = os.path.join(module_path,'input.txt')


with open(python_path, 'r') as file:
    # Read all lines from the file into a list
    file_contents = file.readlines()


counter = 0
total = 0

# df = pd.DataFrame(file_contents)

for i in file_contents:
    counter += 1
    result = i.split(';')
    false = 0

    pattern_green = r'(\d+)\s+green'
    pattern_red = r'(\d+)\s+red'
    pattern_blue = r'(\d+)\s+blue'

    max_green = 0
    max_red = 0
    max_blue = 0
    # Use re.search to find the pattern in the string
    for j in result:
        print(j)
        match_green = re.search(pattern_green, j)

        if match_green:
        # Extract the number before 'green'
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
    
print(total)