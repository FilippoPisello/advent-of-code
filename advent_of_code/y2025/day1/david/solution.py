"""Solution for day 1 of Advent of Code 2025, by david."""


def main_part_one(problem_input: str) -> None:

    dial_a = 50
    solution_1 = 0

    for line in problem_input.splitlines():

        dial = int(line.replace("L", "-").replace("R", ""))
        dial_b = dial_a + dial

        if dial_b % 100 == 0:
            solution_1 += 1

        dial_a = dial_b

    print(solution_1)


def main_part_two(problem_input: str) -> None:

    dial_a = 50
    solution_2 = 0

    for line in problem_input.splitlines():

        dial = int(line.replace("L", "-").replace("R", ""))
        dial_b = dial_a + dial

        if dial_a % 100 == 0:
            solution_2 += abs(dial) // 100
        elif dial_b % 100 == 0:
            solution_2 += 1 + abs(dial) // 100
        else:
            solution_2 += abs(dial_a // 100 - dial_b // 100)

        dial_a = dial_b

    print(solution_2)
