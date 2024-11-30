mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main(problem_input: list[str]):
    
    total_numbers = 0
    total_letters = 0
    
    for line in problem_input:
        
        numbers = []
        letters = []

        for _, char in enumerate(line):
            if char.isdigit():
                numbers.append(char)
        first_last_number = int(numbers[0] + numbers[len(numbers)-1])
        total_numbers += first_last_number              
        
        for word, number in mapping.items():
            index = line.find(word)
            while index != -1:
                line = line[:index + 1] + number + line[index + 2:]
                index = line.find(word, index + 1)
        
        for _, char in enumerate(line):
            if char.isdigit():
                letters.append(char)
        first_last_letter = int(letters[0] + letters[len(letters)-1])
        total_letters += first_last_letter            
                
    return total_numbers, total_letters
