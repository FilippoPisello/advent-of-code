"""Test part 2 with the example from the problem."""

from solution import is_invalid_id_part_two, main_part_two

# Test individual invalid IDs from the problem
test_cases = [
    (11, True),      # "1" × 2
    (22, True),      # "2" × 2
    (99, True),      # "9" × 2
    (111, True),     # "1" × 3
    (999, True),     # "9" × 3
    (1010, True),    # "10" × 2
    (565656, True),  # "56" × 3
    (824824824, True),      # "824" × 3
    (2121212121, True),     # "21" × 5
    (12341234, True),       # "1234" × 2
    (123123123, True),      # "123" × 3
    (1212121212, True),     # "12" × 5
    (1111111, True),        # "1" × 7
    (101, False),    # Not a repeated pattern
    (1001, False),   # "10" + "01" - second half has leading zero
    (123, False),    # Not repeated
]

print("Testing individual cases:")
for num, expected in test_cases:
    result = is_invalid_id_part_two(num)
    status = "✓" if result == expected else "✗"
    print(f"{status} {num}: {result} (expected {expected})")

# Test with the full example
example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

print("\nTesting full example (expected sum: 4174379265):")
main_part_two(example_input)
