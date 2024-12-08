"""Solution for day 8 of Advent of Code 2024, by max."""

from typing import Any, List
import copy


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(str(line)) for line in lines]

    antenas = _parse_unique_antenas(grid)

    recorded_nodes = set() 

    for antena in antenas:
        antena_grid = _build_antena_grid(copy.deepcopy(grid), antena)
        coordinates = _parse_antena_coordinates(antena_grid, antena)

        for i, coordinate in enumerate(coordinates):
            ref_row, ref_col = coordinate

            for j, comparison in enumerate(coordinates[i+1:], start=i+1):  # Avoid duplicate checks
                comp_row, comp_col = comparison

                node_ref_row, node_ref_col = ref_row - (comp_row - ref_row), ref_col - (comp_col - ref_col)
                node_comp_row, node_comp_col = comp_row + (comp_row - ref_row), comp_col + (comp_col - ref_col)

                if (node_ref_row, node_ref_col) not in recorded_nodes and _is_in_range(antena_grid, node_ref_row, node_ref_col):
                    recorded_nodes.add((node_ref_row, node_ref_col))
                
                if (node_comp_row, node_comp_col) not in recorded_nodes and _is_in_range(antena_grid, node_comp_row, node_comp_col):
                    recorded_nodes.add((node_comp_row, node_comp_col))

    return len(recorded_nodes)

def _is_in_range(grid: List[List[str]], row: int, column: int) -> bool:
    return (0 <= row < len(grid) and 0 <= column < len(grid[0]))
    
def _parse_unique_antenas(grid: List[List[str]]) -> List[str]:
    antenas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".": 
                antenas.append(grid[row][col])
    
    return list(set(antenas))

def _build_antena_grid(grid: List[List[str]], antena: str) -> List[List[str]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != antena: 
                grid[row][col] = '.'
    
    return grid

def _parse_antena_coordinates(grid: List[List[str]], antena: str) -> List[tuple[int, int]]:
    coordinates = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == antena: 
                coordinates.append((row, col))
    
    return coordinates



def main_part_two(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    grid = [list(str(line)) for line in lines]

    antenas = _parse_unique_antenas(grid)
    recorded_nodes = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".": 
                recorded_nodes.add((row, col)) 

    for antena in antenas:
        antena_grid = _build_antena_grid(copy.deepcopy(grid), antena)
        coordinates = _parse_antena_coordinates(antena_grid, antena)

        for i, coordinate in enumerate(coordinates):
                print({coordinate})
                ref_row, ref_col = coordinate

                for j, comparison in enumerate(coordinates[i+1:], start=i+1):  # Avoid duplicate checks
                    comp_row, comp_col = comparison

                    node_ref_row, node_ref_col = ref_row - (comp_row - ref_row), ref_col - (comp_col - ref_col)
                    while _is_in_range(antena_grid, node_ref_row, node_ref_col):
                        if (node_ref_row, node_ref_col) not in recorded_nodes:
                            recorded_nodes.add((node_ref_row, node_ref_col))
                        node_ref_row -= (comp_row - ref_row)
                        node_ref_col -= (comp_col - ref_col)

                    node_comp_row, node_comp_col = comp_row + (comp_row - ref_row), comp_col + (comp_col - ref_col)
                    while _is_in_range(antena_grid, node_comp_row, node_comp_col):
                        if (node_comp_row, node_comp_col) not in recorded_nodes:
                            recorded_nodes.add((node_comp_row, node_comp_col))
                        node_comp_row += (comp_row - ref_row)
                        node_comp_col += (comp_col - ref_col)
                
    return len(recorded_nodes)

# def main(problem_input: str) -> Any:
#    return
