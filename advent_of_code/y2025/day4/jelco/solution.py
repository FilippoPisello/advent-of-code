"""Solution for day 4 of Advent of Code 2025, by jelco."""


def count_accessible_rolls(grid: list[str]) -> int:
    """
    Count how many paper rolls are accessible by forklifts.

    A roll (@) is accessible if it has fewer than 4 neighboring rolls
    in the 8 adjacent positions (including diagonals).

    Args:
        grid: List of strings representing the warehouse grid

    Returns:
        Number of accessible rolls
    """
    # 8 directions: NW, N, NE, W, E, SW, S, SE
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
        (0, -1),           (0, 1),   # W,     E
        (1, -1),  (1, 0),  (1, 1),   # SW, S, SE
    ]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible_count = 0

    # Check each position in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                # Count neighboring rolls
                neighbor_count = 0

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    # Check if neighbor is in bounds and is a roll
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            neighbor_count += 1

                # Roll is accessible if it has fewer than 4 neighbors
                if neighbor_count < 4:
                    accessible_count += 1

    return accessible_count


def main_part_one(problem_input: str) -> None:
    """Solve part one of the problem."""
    grid = problem_input.strip().split('\n')
    result = count_accessible_rolls(grid)
    print(result)


def find_accessible_positions(grid: list[list[str]]) -> list[tuple[int, int]]:
    """
    Find all positions with accessible rolls.

    Args:
        grid: Mutable 2D grid (list of lists)

    Returns:
        List of (row, col) tuples for accessible rolls
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
        (0, -1),           (0, 1),   # W,     E
        (1, -1),  (1, 0),  (1, 1),   # SW, S, SE
    ]

    accessible = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                neighbor_count = 0

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            neighbor_count += 1

                if neighbor_count < 4:
                    accessible.append((i, j))

    return accessible


def count_removable_rolls(grid: list[str]) -> int:
    """
    Count total rolls that can be removed by iterative removal.

    Repeatedly finds and removes accessible rolls until none remain.

    Args:
        grid: List of strings representing the warehouse grid

    Returns:
        Total number of rolls that can be removed
    """
    # Convert to mutable structure
    grid = [list(row) for row in grid]

    total_removed = 0

    while True:
        # Find all accessible rolls in current state
        accessible = find_accessible_positions(grid)

        if not accessible:
            break

        # Remove all accessible rolls
        for i, j in accessible:
            grid[i][j] = '.'

        total_removed += len(accessible)

    return total_removed


def main_part_two(problem_input: str) -> None:
    """Solve part two of the problem."""
    grid = problem_input.strip().split('\n')
    result = count_removable_rolls(grid)
    print(result)
