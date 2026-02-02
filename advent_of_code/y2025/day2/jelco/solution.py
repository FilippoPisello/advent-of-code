"""Solution for day 2 of Advent of Code 2025, by jelco."""


def is_invalid_id(num: int) -> bool:
    """
    Check if a number is an invalid ID.

    An invalid ID is a number made of some sequence of digits repeated twice.
    Examples: 11 (1+1), 6464 (64+64), 123123 (123+123)

    The repeated pattern cannot start with 0 (no leading zeroes).
    """
    num_str = str(num)
    length = len(num_str)

    # Must have even length to be split into two equal halves
    if length % 2 != 0:
        return False

    # Split in half
    mid = length // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]

    # Check if both halves are identical and first half doesn't start with 0
    return first_half == second_half and first_half[0] != '0'


def main_part_one(problem_input: str) -> None:
    """Solve part one of the problem."""
    # Parse the input to get ranges
    ranges_str = problem_input.strip()
    range_parts = ranges_str.split(',')

    total_sum = 0

    # Process each range
    for range_part in range_parts:
        start, end = map(int, range_part.split('-'))

        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num

    print(total_sum)


def is_invalid_id_part_two(num: int) -> bool:
    """
    Check if a number is an invalid ID for part two.

    An invalid ID is a number made of some sequence of digits repeated at least twice.
    Examples: 12341234 (1234×2), 123123123 (123×3), 1212121212 (12×5), 1111111 (1×7)

    The repeated pattern cannot start with 0 (no leading zeroes).
    """
    num_str = str(num)
    length = len(num_str)

    # Try all possible pattern lengths from 1 to length/2
    for pattern_length in range(1, length // 2 + 1):
        # Check if the number length is divisible by pattern length
        if length % pattern_length == 0:
            pattern = num_str[:pattern_length]

            # Pattern cannot start with 0 (no leading zeroes)
            if pattern[0] == '0':
                continue

            # Check if the entire number is made of this pattern repeated
            num_repetitions = length // pattern_length
            if pattern * num_repetitions == num_str and num_repetitions >= 2:
                return True

    return False


def main_part_two(problem_input: str) -> None:
    """Solve part two of the problem."""
    # Parse the input to get ranges
    ranges_str = problem_input.strip()
    range_parts = ranges_str.split(',')

    total_sum = 0

    # Process each range
    for range_part in range_parts:
        start, end = map(int, range_part.split('-'))

        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id_part_two(num):
                total_sum += num

    print(total_sum)
