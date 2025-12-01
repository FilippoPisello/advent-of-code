# capacity, stack from 1 to 4
# Temp(A) > Temp(C) > Temp(F)
# heavier < lighter

# Handling cost
## 1 --> 50, 2 --> 25, 3 --> 10, 4 --> 0

import os


def read_local_input_file():
    # Determine the absolute path of input.txt relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "input.txt")

    # Read the file content safely
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    return data


# def main_part_one() -> None:
problem_input = read_local_input_file().split()
problem_formated = []
dict_temp = {"A": 1, "C": 2, "F": 3}

for i in problem_input:
    problem_formated.append(str(dict_temp[i[0]]) + i[1:])


print(problem_formated)
