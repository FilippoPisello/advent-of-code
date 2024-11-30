import os
import helper

# module_path = os.path.dirname(os.path.abspath(__file__))
# python_path = os.path.join(module_path,'advent/jour_1.txt')

python_path = r"/home/lxwat/picnic-analytical-tools/merchandising_systems_ms/FR-RetrieveASN/advent/sacha_jour_1.txt"
with open(python_path, 'r') as file:
    # Read all lines from the file into a list
    file_contents = file.readlines()


# print(file_contents)
list_number = []
counter = 0
total = 0
for i in file_contents:

    string = helper.replace_string_to_int(i)
    first_digit = helper.get_first_digit(string)
    last_digit = helper.get_last_digit(string)
    # list_number[counter].append(first_digit)
    # list_number[counter].append(last_digit)
    counter += 1
    number = int(str(first_digit) + str(last_digit))
    total += number

    # print(string)

print(total)
# print(list_number)
