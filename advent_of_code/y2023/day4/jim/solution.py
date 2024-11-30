import re

def main(problem_input: list[str]):
    
    key = 1
    pattern = r'(\d+)'
    game_dict = {}
    total_reward = 0

    # Create reward dict
    reward_dict = {0: 0, 1: 1}
    result = 1 
    for i in range(2,100):
        result = result * 2
        reward_dict[i] = result

    # Loop through lines, reformat and add to games dict
    for line in problem_input:
        line = line.replace(line[:10], "") #change to 10 with big set
        line = line.split("|")
        game_dict[key] = line
        key += 1

    ## Part One
    # Find matches and add to total
    for key, game in game_dict.items():
        total = 0 
        winning_numbers = re.findall(pattern, game[0])
        actual_numbers = re.findall(pattern, game[1])
        for i in winning_numbers:
            for j in actual_numbers:
                if i == j:
                    total += 1     
        total_reward += reward_dict[total]
        game_dict[key] = total

    ## Part two
    # Create copy dict with one copy per card initially
    copies = {}
    for i in game_dict:
        copies[i] = 1
    
    # Loop through the cards in games dict 
    for current_card, number_of_matching_numbers in game_dict.items():
        
        # If a card has x matching numbers, yout receive a copy of the x consecutive cards
        consecutive_card = current_card + 1
        last_card = current_card + number_of_matching_numbers
        
        # For every card, iterate through the received copies of consecutive cards 
        for copy in range(consecutive_card, last_card + 1):
            try:
                # Add to the copy dictionary, the number of instances you have of the 
                # current card: if you have two instances of a card, and the card in 
                # question has 3 matching numbers, you will receive TWO copies of the 
                # three consecutive cards (because you have two instances)
                copies[copy] += copies[current_card]
            except KeyError:
                # Cards will never make you copy a card past the end of the table
                continue
                    
    return total_reward, sum(copies.values())