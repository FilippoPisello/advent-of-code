from pathlib import Path

from advent_of_code import read_txt_input


def main():
    text = read_txt_input(1)
    output = run(text)
    print(output)


mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def run(text: list[str]) -> str:
    total = 0
    for line in text:
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


if __name__ == "__main__":
    main()
