def main_part_one(problem_input: list[str]):

    import re

    input_list = input_str.split('\n')

    final_list = []
    for string in input_list:
        pattern = re.compile(r'\d')
        numbers_found = pattern.findall(string)
        final_list.append(numbers_found)

    answer = 0
    for list_i in final_list:
        number = int(''.join([list_i[0], list_i[-1]]))
        answer += number

    print(answer)

def main_part_two(problem_input: list[str]):
    input_list = lines = input_str.split('\n')

    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    def main(problem_input: list[str]):
        total = 0
        for line in problem_input:
            matches = {}

            for spelled_out_digit, digit in mapping.items():
                newstring = line.replace(spelled_out_digit, "!" * len(spelled_out_digit))
                for index, char in enumerate(newstring):
                    if char == "!":
                        matches[index] = digit

            for index, char in enumerate(line):
                if char.isdigit():
                    matches[index] = int(char)

            if not matches:
                number = 0
            else:
                matches = sorted(matches.items(), key=lambda x: x[0])
                number = int(f"{matches[0][1]}{matches[-1][1]}")
            total += number

        return str(total)

    print(main(input_list))
