from dataclasses import dataclass


@dataclass
class Card:
    card_id: str
    winning_num: list[int]
    game_num: list


def main(problem_input: list[str]):
    cards = map_card(problem_input)
    count_total = 0
    scratch_card = [1] * len(problem_input)
    for id, card in enumerate(cards):
        count_card = 0
        count_win = 0
        for num in card.game_num:
            if num in card.winning_num:
                count_card = max(count_card * 2, 1)
                count_win += 1
        for x in range(count_win):
            if (id + x + 1) < len(problem_input):
                scratch_card[id + x + 1] += scratch_card[id]
        count_total += count_card

    return count_total, sum(scratch_card)


def map_card(problem_input: list[str]) -> list[Card]:
    cards: list[dict[Card, int]] = []
    for line in problem_input:
        num = line.split(":")[1].split("|")
        cards.append(
            Card(
                card_id=line.split(":")[0],
                winning_num=[int(x) for x in num[0].split()],
                game_num=[int(x) for x in num[1].split()],
            )
        )
    return cards
