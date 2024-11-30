import pandas as pd
import re

with open('input.txt', 'r') as file:
    content  = file.read()
    modified_content = content.replace('seeds:', 'seeds:\n')

with open('new_input.txt', 'w') as file:
    file.write(modified_content)

with open('new_input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

def input_formatting(input : list):
    list_of_var = []
    word_count = 0
    dico ={}
    for line in input : 
        if any(c.isalpha() for c in line):
            key = str(line)
            dico[key]=[]
            word_count +=1
            list_of_var.append(key)
        else:
            key = list_of_var[-1]
            list_nb_str = separate_numbers(line)
            list_nb = [int(element) for element in list_nb_str if element != '']
            dico[key].append(list_nb)
    seeds_var = list_of_var[0]
    dico[seeds_var] = list_fusion(dico[seeds_var])
    return(dico, list_of_var)

def correspondance(nb : int, window : list): #destination source length
    if nb != None:
        if window != []:
            destination_start = window[0]
            source_start = window[1]
            length = window[2]
            if nb >= source_start and nb <= source_start+length-1:
                position = nb - source_start + 1
                destination_nb = destination_start + position -1
            else:
                destination_nb = nb
            return destination_nb

def matching(source : list, destination :list):
    output_list_nb = []
    for element in source:
        for map in destination:
            destination_nb = correspondance (element, map)
            output_list_nb.append(destination_nb)
    return output_list_nb

def separate_numbers(line_input : str):
    nb = line_input.split(' ')
    return nb

def list_fusion(list_of_lists : int):
    final_list = list_of_lists[0]
    for i in range (1, len(list_of_lists)):
        final_list += list_of_lists[i]
    return final_list


def main_part_one(problem_input: list[str]):
    dico_var, list_var = input_formatting(problem_input)
    seeds_var = list_var[0]
    list_final = dico_var[seeds_var]
    for var_num in range(1, len(list_var)):
        var = list_var[var_num]
        map = dico_var[var]
        list_final = matching(list_final, map)
    return min(list_final)

    return dico_var, list_var

print(main_part_one(lines))
#print(matching([36], [[40, 30, 11]]))
