# Day 2: Invalid Product IDs - Solution Approach

## Problem Summary
Find all "invalid" product IDs within given ranges and sum them up. An invalid ID is a number composed of some sequence of digits repeated exactly twice.

## Examples of Invalid IDs
- `11` = "1" repeated twice
- `6464` = "64" repeated twice
- `123123` = "123" repeated twice
- `1010` = "10" repeated twice
- `222222` = "222" repeated twice

## Key Observations

1. **Even Length Requirement**: All invalid IDs must have an even number of digits (to be split into two equal halves)

2. **Pattern Matching**: The first half of digits must exactly match the second half

3. **No Leading Zeroes**: The repeated pattern cannot start with 0
   - Example: `1001` is NOT invalid (would be "10" + "01", but "01" has leading zero)
   - This ensures we don't count patterns that would imply leading zeroes

## Algorithm

### Step 1: Parse Input
- Read the input line
- Split by commas to get individual ranges
- For each range, split by dash to get start and end values

### Step 2: Check if Number is Invalid
For a given number:
```
1. Convert to string
2. Check if length is even
3. If even:
   - Split string in half
   - Check if first_half == second_half
   - Check if first_half doesn't start with '0'
4. If all conditions met, it's invalid
```

### Step 3: Process Each Range
For each range [start, end]:
```
1. Iterate through all numbers from start to end (inclusive)
2. Check if each number is invalid
3. Collect all invalid IDs
```

### Step 4: Sum Results
Add up all invalid IDs found across all ranges

## Complexity Considerations

### Optimization Needed?
Given that ranges can be very large (e.g., 824824821-824824827), we need to consider:
- **Brute Force**: Check every number in every range
  - Simple but could be slow for large ranges
  - However, based on example ranges, most are relatively small

- **Pattern Generation**: Generate all possible repeated patterns
  - For a range, calculate which repeated patterns fall within it
  - More complex but potentially faster for very large ranges

### Initial Approach: Brute Force
Start with brute force since:
1. Most ranges in the example are small (< 10 numbers)
2. The check for invalidity is O(1) for each number
3. Can optimize later if needed

## Implementation Steps

1. **Part 1**:
   - Parse input ranges
   - Implement `is_invalid(num)` function
   - Iterate through all ranges and numbers
   - Sum all invalid IDs
   - Return the sum

2. **Part 2**:
   - Wait for part 2 instructions (usually a variation of part 1)

## Test Cases (from problem)
- Range `11-22`: Invalid IDs = [11, 22]
- Range `95-115`: Invalid IDs = [99]
- Range `998-1012`: Invalid IDs = [1010]
- Range `1188511880-1188511890`: Invalid IDs = [1188511885]
- Range `222220-222224`: Invalid IDs = [222222]

Expected sum: 1227775554
