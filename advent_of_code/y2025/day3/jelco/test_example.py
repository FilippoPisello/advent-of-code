"""Test with the example from the problem."""

from solution import find_max_joltage, main_part_one

# Test individual banks
test_cases = [
    ("987654321111111", 98),   # positions 0,1 → 9,8 → 98
    ("811111111111119", 89),   # positions 0,14 → 8,9 → 89
    ("234234234234278", 78),   # positions 13,14 → 7,8 → 78
    ("818181911112111", 92),   # positions 6,11 → 9,2 → 92
]

print("Testing individual banks:")
for bank, expected in test_cases:
    result = find_max_joltage(bank)
    status = "✓" if result == expected else "✗"
    print(f"{status} {bank}: {result} (expected {expected})")

# Test with the full example
example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

print("\nTesting full example (expected sum: 357):")
main_part_one(example_input)
