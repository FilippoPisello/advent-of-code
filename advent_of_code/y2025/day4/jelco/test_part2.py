"""Test part 2 with the example from the problem."""

from solution import count_removable_rolls

example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

grid = example_input.split('\n')
result = count_removable_rolls(grid)

print(f"Total removable rolls: {result}")
print(f"Expected: 43")
print(f"Status: {'✓ PASS' if result == 43 else '✗ FAIL'}")
