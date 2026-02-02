# Day 3: Lobby - Solution Approach

## Problem Summary
Find the maximum joltage each battery bank can produce by selecting exactly two batteries, then sum all maximum joltages.

## Key Rules
1. Each line is a bank of batteries (digits 1-9)
2. Must turn on exactly **two batteries** per bank
3. Joltage = two-digit number formed by selected batteries (in original order)
4. Cannot rearrange batteries - order matters
5. Goal: Maximize joltage for each bank, then sum

## Examples

### Bank: `987654321111111`
- Best pair: positions 0,1 → batteries 9,8 → **98 jolts**

### Bank: `811111111111119`
- Best pair: positions 0,14 → batteries 8,9 → **89 jolts**

### Bank: `234234234234278`
- Best pair: positions 13,14 → batteries 7,8 → **78 jolts**

### Bank: `818181911112111`
- Best pair: positions 6,11 → batteries 9,2 → **92 jolts**

**Total: 98 + 89 + 78 + 92 = 357**

## Algorithm

### Part 1: Find Maximum Joltage Per Bank

For each bank (line):
```
1. Initialize max_joltage = 0
2. For each pair of positions (i, j) where i < j:
   a. Calculate joltage = digit[i] * 10 + digit[j]
   b. Update max_joltage if this is larger
3. Add max_joltage to total sum
```

### Optimization Considerations

**Brute Force Approach:**
- For a bank of length n, there are n*(n-1)/2 pairs to check
- For most inputs, banks won't be extremely long
- Time complexity: O(n²) per bank, where n is bank length
- This should be fast enough

**Potential Optimization (if needed):**
- To maximize a two-digit number XY:
  - Want largest X (tens place) as possible
  - Then want largest Y (ones place) that comes after X
- Could iterate through digits to find largest, then find largest after it
- But brute force is simpler and likely fast enough

### Initial Approach: Brute Force
Start with checking all pairs since:
1. Implementation is straightforward
2. Should be performant for typical input sizes
3. Easy to verify correctness

## Implementation Steps

1. **Part 1**:
   - Parse input (each line is a bank)
   - For each bank:
     - Try all pairs of positions (i < j)
     - Calculate joltage = int(bank[i]) * 10 + int(bank[j])
     - Track maximum joltage
   - Sum all maximum joltages
   - Return total

2. **Part 2**: Select exactly **12 batteries** per bank to form maximum 12-digit number

   **Greedy Algorithm:**
   - We need to select 12 digits from n total digits
   - Can skip (n - 12) digits
   - At each position in result, choose the largest digit from a valid window
   - Window: start from current position, can look ahead by skip_remaining positions

   **Process:**
   ```
   For each of 12 positions to fill:
     1. Calculate window end: current + skip_remaining + 1
     2. Find maximum digit in window [current:end]
     3. Add that digit to result
     4. Update skip_remaining (subtract skipped positions)
     5. Move current position to after selected digit
   ```

   **Example trace for "234234234234278" → "434234234278":**
   - Total: 15 digits, need: 12, can skip: 3
   - Position 0: Window [0:4]="2342", pick '4' at index 3, skip 3 digits
   - Position 1: Window [4:5]="3", pick '3' at index 4, skip 0 digits
   - Positions 2-11: No more skips, take next 10 digits
   - Result: "434234234278" ✓

## Test Cases (from problem)

### Part 1 Example:
```
987654321111111
811111111111119
234234234234278
818181911112111
```

**Expected Results:**
- Bank 1: 98 jolts
- Bank 2: 89 jolts
- Bank 3: 78 jolts
- Bank 4: 92 jolts
- **Total: 357 jolts**

### Part 2 Example (same input):

**Expected Results:**
- Bank 1: 987654321111 (skip last 3 ones)
- Bank 2: 811111111119 (skip 3 middle ones)
- Bank 3: 434234234278 (skip 2,3,2 near start)
- Bank 4: 888911112111 (skip some ones)
