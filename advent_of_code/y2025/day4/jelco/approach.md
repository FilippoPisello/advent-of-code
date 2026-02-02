# Day 4: Printing Department - Solution Approach

## Problem Summary
Count how many rolls of paper (`@`) can be accessed by forklifts. A roll is accessible if it has **fewer than 4** neighboring rolls in the 8 adjacent positions.

## Key Rules
1. Grid contains:
   - `@` = roll of paper
   - `.` = empty space

2. **Accessibility condition:** A roll at position (i, j) is accessible if:
   - Count of `@` symbols in its 8 neighbors < 4

3. **8 neighbors (including diagonals):**
   ```
   NW  N  NE
    W  @  E
   SW  S  SE
   ```

## Example Analysis

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Accessible rolls (marked with x):**
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Example traces:**

Position (0,2) = `@`:
- Neighbors: (0,1)=`.`, (0,3)=`@`, (1,1)=`@`, (1,2)=`@`, (1,3)=`.`
- Count of `@`: 3 < 4 → **Accessible** ✓

Position (1,1) = `@`:
- Neighbors: (0,0)=`.`, (0,1)=`.`, (0,2)=`@`, (1,0)=`@`, (1,2)=`@`, (2,0)=`@`, (2,1)=`@`, (2,2)=`@`
- Count of `@`: 6 ≥ 4 → **Not accessible** ✗

## Algorithm

### Part 1: Count Accessible Rolls

```
1. Parse input into 2D grid
2. Initialize accessible_count = 0
3. For each position (i, j) in grid:
   a. If grid[i][j] == '@':
      i. Count neighbors = 0
      ii. For each of 8 directions:
          - Check if neighbor position is valid (in bounds)
          - If neighbor is '@', increment count
      iii. If count < 4:
           - accessible_count += 1
4. Return accessible_count
```

### 8 Directions (relative offsets):
```python
directions = [
    (-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
    ( 0, -1),          ( 0, 1),  # W,     E
    ( 1, -1), ( 1, 0), ( 1, 1),  # SW, S, SE
]
```

## Implementation Steps

1. **Part 1**:
   - Parse grid into list of lists or strings
   - For each `@` position:
     - Count `@` neighbors (8 directions)
     - If count < 4, it's accessible
   - Return total accessible count

2. **Part 2**: Iteratively remove accessible rolls until none remain

   **Modified Algorithm:**
   - Instead of just counting, we need to simulate the removal process
   - Each iteration:
     1. Find all accessible rolls (< 4 neighbors)
     2. Remove them all (convert to '.')
     3. Repeat until no accessible rolls remain
   - Count total rolls removed across all iterations

   **Process:**
   ```
   1. Convert grid to mutable structure (list of lists)
   2. Initialize total_removed = 0
   3. While True:
      a. Find all positions with accessible rolls
      b. If no accessible rolls found, break
      c. Remove all accessible rolls (set to '.')
      d. Add count to total_removed
   4. Return total_removed
   ```

   **Key difference from Part 1:**
   - Part 1: Count accessible rolls once
   - Part 2: Repeatedly find and remove accessible rolls until none remain
   - Removing rolls changes the neighbor counts for nearby rolls

## Complexity
- **Time:** O(rows × cols × 8) = O(rows × cols)
- **Space:** O(rows × cols) for storing grid

## Test Case (from problem)

### Example Input:
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Expected Result:** 13 accessible rolls
