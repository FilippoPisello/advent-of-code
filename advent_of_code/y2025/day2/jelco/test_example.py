"""Test with the example from the problem."""

from solution import is_invalid_id, main_part_one

# Test individual invalid IDs from the problem
test_cases = [
    (11, True),   # "1" + "1"
    (22, True),   # "2" + "2"
    (99, True),   # "9" + "9"
    (1010, True), # "10" + "10"
    (1188511885, True),  # "11885" + "11885"
    (222222, True),      # "222" + "222"
    (446446, True),      # "446" + "446"
    (38593859, True),    # "3859" + "3859"
    (101, False),  # Not a repeated pattern
    (1001, False), # "10" + "01" - second half has leading zero
]

print("Testing individual cases:")
for num, expected in test_cases:
    result = is_invalid_id(num)
    status = "✓" if result == expected else "✗"
    print(f"{status} {num}: {result} (expected {expected})")

# Test with the full example
example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

print("\nTesting full example (expected sum: 1227775554):")
main_part_one(example_input)
