def get_last_digit(s):
    for char in reversed(s):
        if char.isdigit():
            return int(char)
    return None  # Return None if no digit is found in the string


def get_first_digit(s):
    for char in s:
        if char.isdigit():
            return int(char)
    return None  # Return None if no digit is found in the string

def replace_string_to_int(s):
    replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for old, new in replacements.items():
        if old in s:
         index = s.find(old)
         while index != -1:
          s = s[:index + 1] + new + s[index + 2:]
          index = s.find(old, index + 1)

    return s
