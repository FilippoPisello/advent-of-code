def main_part_one(problem_input: list[str]):
    total = 0
    parsed_input = parse_problem_info(problem_input)
    for number_of_winning_and_owned in parsed_input.values():
        if not number_of_winning_and_owned:
            continue
        score = 2 ** (number_of_winning_and_owned - 1)
        total += score
    return total


def main_part_two(problem_input: list[str]):
    parsed_input = parse_problem_info(problem_input)
    copies = {card_number: 1 for card_number in parsed_input}
    for card_number, number_of_winning_and_owned in parsed_input.items():
        next_card_number = card_number + 1
        last_affected_card_number = card_number + number_of_winning_and_owned
        for copy in range(next_card_number, last_affected_card_number + 1):
            try:
                copies[copy] += 1 * copies[card_number]
            except KeyError:
                continue
    return sum(copies.values())


def parse_problem_info(problem_input: list[str]) -> dict[str, int]:
    output = {}
    for card_number, line in enumerate(problem_input, start=1):
        _, line_without_card = line.split(":")

        winning, owned = line_without_card.split("|")
        winning = set(int(n) for n in winning.split())
        owned = set(int(n) for n in owned.split())

        output[card_number] = len(winning & owned)

    return output
