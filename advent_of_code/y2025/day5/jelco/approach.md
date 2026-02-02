# Day 5: Cafeteria - Approach

## Problem Summary
- Given a list of fresh ingredient ID ranges (e.g., `3-5`, `10-14`)
- Given a list of available ingredient IDs
- Determine which available IDs fall within any fresh range
- Count how many are fresh

## Part 1 Approach
1. Parse the input:
   - Split by blank line to separate ranges from ingredient IDs
   - Parse ranges into (start, end) tuples
   - Parse ingredient IDs into integers
2. For each ingredient ID:
   - Check if it falls within any range (inclusive)
   - A range `a-b` includes all integers from a to b
3. Count the fresh ingredients

## Complexity
- Time: O(n * m) where n = number of ingredient IDs, m = number of ranges
- Space: O(n + m)

## Part 2
- Ignore the available ingredient IDs (second section)
- Find ALL ingredient IDs that are considered fresh according to the ranges
- Need to handle overlapping ranges to avoid double counting

### Approach
1. Parse only the ranges (ignore second section)
2. Merge overlapping ranges:
   - Sort ranges by start position
   - Iterate and merge overlapping/adjacent ranges
3. Count total IDs in all merged ranges: sum of (end - start + 1) for each range

### Example
Ranges: 3-5, 10-14, 16-20, 12-18
- After merging: 3-5, 10-20
- Count: (5-3+1) + (20-10+1) = 3 + 11 = 14
