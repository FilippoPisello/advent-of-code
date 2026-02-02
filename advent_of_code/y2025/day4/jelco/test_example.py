"""Test part 1 with the example from the problem."""

from solution import count_accessible_rolls

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
result = count_accessible_rolls(grid)

print(f"Accessible rolls: {result}")
print(f"Expected: 13")
print(f"Status: {'✓ PASS' if result == 13 else '✗ FAIL'}")
