"""Test part 2 with the example from the problem."""

from solution import find_max_joltage_k_batteries, main_part_two

# Test individual banks with k=12
test_cases = [
    ("987654321111111", 987654321111),   # Skip last 3 ones
    ("811111111111119", 811111111119),   # Skip 3 middle ones
    ("234234234234278", 434234234278),   # Skip 2,3,2 near start
    ("818181911112111", 888911112111),   # Skip some ones
]

print("Testing individual banks (k=12):")
for bank, expected in test_cases:
    result = find_max_joltage_k_batteries(bank, 12)
    status = "✓" if result == expected else "✗"
    print(f"{status} {bank}: {result} (expected {expected})")

# Test with the full example
example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

print("\nTesting full example:")
print("Expected banks:")
print("- 987654321111")
print("- 811111111119")
print("- 434234234278")
print("- 888911112111")
print("\nCalculating total:")
main_part_two(example_input)
