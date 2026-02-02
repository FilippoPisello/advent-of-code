"""Solution for day 3 of Advent of Code 2025, by jelco."""


def find_max_joltage(bank: str) -> int:
    """
    Find the maximum joltage possible from a battery bank.

    The joltage is the two-digit number formed by selecting exactly two
    batteries (in their original order).

    Args:
        bank: String of digits representing battery joltages

    Returns:
        Maximum joltage possible from this bank
    """
    max_joltage = 0

    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Calculate joltage: digit[i] is tens place, digit[j] is ones place
            joltage = int(bank[i]) * 10 + int(bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


def main_part_one(problem_input: str) -> None:
    """Solve part one of the problem."""
    banks = problem_input.strip().split('\n')

    total_joltage = 0
    for bank in banks:
        max_joltage = find_max_joltage(bank)
        total_joltage += max_joltage

    print(total_joltage)


def find_max_joltage_k_batteries(bank: str, k: int) -> int:
    """
    Find the maximum joltage by selecting exactly k batteries.

    Uses a greedy algorithm: at each position, select the largest digit
    from a valid window, ensuring we have enough digits remaining.

    Args:
        bank: String of digits representing battery joltages
        k: Number of batteries to select

    Returns:
        Maximum joltage possible (as integer)
    """
    n = len(bank)
    if k > n:
        raise ValueError(f"Cannot select {k} batteries from {n}")

    result = []
    skip_remaining = n - k  # How many digits we can skip
    start = 0  # Current starting position in bank

    for _ in range(k):
        # We can look ahead by skip_remaining positions
        end = start + skip_remaining + 1

        # Find the maximum digit in this window
        window = bank[start:end]
        max_digit = max(window)
        max_index = start + window.index(max_digit)

        # Add this digit to result
        result.append(max_digit)

        # Update for next iteration
        skip_remaining -= (max_index - start)
        start = max_index + 1

    return int(''.join(result))


def main_part_two(problem_input: str) -> None:
    """Solve part two of the problem."""
    banks = problem_input.strip().split('\n')

    total_joltage = 0
    for bank in banks:
        max_joltage = find_max_joltage_k_batteries(bank, 12)
        total_joltage += max_joltage

    print(total_joltage)
