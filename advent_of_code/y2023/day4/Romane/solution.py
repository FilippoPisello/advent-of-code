import pandas as pd
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

cards=[]
for line in lines:
    cards.append(line)


def main_part_one(problem_input: list[str]):
    list_of_cards_elements = create_list_of_cards_elements(cards)
    winning_nb_list = winning_nbs(list_of_cards_elements)
    score_final = score_calculation(winning_nb_list)
    return score_final

def main_part_two(problem_input: list[str]):
    list_cards = create_list_of_cards_elements(problem_input)
    counter_list = get_card_info(list_cards)
    counter_list_with_copy = adding_cards(counter_list)
    final_score = count_final(counter_list_with_copy)
    
    return final_score


def create_list_of_cards_elements(list):
    list_cards =[]
    for element in list:
        card_dico = {}

        card, number = element.rstrip('\n').split(':')
        my_nb_1, winning_nb_1 = number.strip().replace(' ', ',').split('|')

        my_nb_2 = my_nb_1.split(',')
        my_nb = [int(x) for x in my_nb_2 if x.isdigit()]

        winning_nb_2 = winning_nb_1.split(',')
        winning_nb = [int(x) for x in winning_nb_2 if x.isdigit()]

        card_dico['card_nb'] = card
        card_dico['my_nb'] = my_nb
        card_dico['winning_nb'] = winning_nb

        list_cards.append(card_dico)
    return list_cards

def winning_nbs(list_dic):
    winning_nb_list = []
    for dico in list_dic:
        winning_dico = {}
        my_nb = set(dico['my_nb'])
        winning_nb = set(dico['winning_nb'])
        common_nb = list(my_nb.intersection(winning_nb))
        winning_dico['card_nb'] = dico['card_nb']
        winning_dico['common_nb'] = common_nb
        winning_nb_list.append(winning_dico)
    return winning_nb_list

def get_card_info(list_dic):
    winning_nb_list = []
    for dico in list_dic:
        winning_dico = {}
        my_nb = set(dico['my_nb'])
        winning_nb = set(dico['winning_nb'])
        common_nb = list(my_nb.intersection(winning_nb))
        winning_dico['card_nb'] = dico['card_nb']
        winning_dico['common_nb'] = len(common_nb)
        winning_dico['card_nb_int'] = card_nb(winning_dico['card_nb'] )
        winning_dico['counter'] = 1
        winning_nb_list.append(winning_dico)
    return winning_nb_list

def score_calculation(list_winning_dico):
    score = 0
    for dico in list_winning_dico:
        if len(dico['common_nb']) > 0:
            i = len(dico['common_nb'])
            pnts = 2**(i-1)
            score += pnts
    return score


def adding_cards(list_of_card_info):
    for dico_i in range(1,len(list_of_card_info)+1):
        repetition = list_of_card_info[dico_i-1]['counter']
        for r in range (0,repetition):
            nb_winning_nb = list_of_card_info[dico_i-1]['common_nb']
            for k in range (dico_i, min(dico_i + nb_winning_nb, len(list_of_card_info)+1)):
                dico = list_of_card_info[k]
                dico['counter'] += 1
    return list_of_card_info


def card_nb(str):
    regex_nb = r'\d+'
    nb = int(re.search(regex_nb, str).group())
    return nb



def count_final(list_of_card_info):
    score = 0
    for dico_card in list_of_card_info:
        score += dico_card['counter']
    return score


print(main_part_one(cards), main_part_two(cards))


