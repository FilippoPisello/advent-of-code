"""Solution for day 10 of Advent of Code 2025, by max."""

from typing import Any
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def main_part_one(problem_input: str) -> Any:
    lines = problem_input.splitlines()
    total_presses = 0

    for i, line in enumerate(lines):
        print(f"Processing line: {i+1} / {len(lines)}")
        starting_lights = tuple(c == "#" for c in line.split(" ")[0].strip("[]"))
        schematics = [
            tuple(map(int, schematic.strip("()").split(",")))
            for schematic in line.split(" ")[1:-1]
        ]
        target = tuple(False for _ in starting_lights)

        if starting_lights == target:
            continue  # Already all off, 0 presses needed

        visited = {starting_lights}
        queue = [(starting_lights, 0)]
        min_presses = None

        while queue and min_presses is None:
            state, presses = queue.pop(0)

            for schematic in schematics:
                new_state = list(state)
                for idx in schematic:
                    new_state[idx] = not new_state[idx]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, presses + 1))

                if new_state == target:
                    min_presses = presses + 1
                    break

        total_presses += min_presses

    return total_presses


def main_part_two(problem_input: str) -> Any:
    """
    Solve using Integer Linear Programming (ILP).

    Problem: Find non-negative integers x_j (press counts for each schematic)
    such that A @ x = target, minimizing sum(x).

    This is a classic ILP problem that scipy.optimize.milp can solve efficiently.
    """
    lines = problem_input.splitlines()
    total_presses = 0

    for i, line in enumerate(lines):
        print(f"Processing line: {i+1} / {len(lines)}")
        target_joltages = list(map(int, line.split(" ")[-1].strip("{}").split(",")))
        schematics = [
            tuple(map(int, schematic.strip("()").split(",")))
            for schematic in line.split(" ")[1:-1]
        ]

        # Build the schematic matrix A where A[position, schematic] = 1 if schematic affects position
        num_positions = len(target_joltages)
        num_schematics = len(schematics)

        A = np.zeros((num_positions, num_schematics), dtype=float)
        for j, schematic in enumerate(schematics):
            for idx in schematic:
                A[idx, j] = 1.0

        target = np.array(target_joltages, dtype=float)

        # Objective: minimize sum of all press counts (coefficients all 1)
        c = np.ones(num_schematics)

        # Constraints: A @ x == target (equality constraint)
        # LinearConstraint(A, lb, ub) means lb <= A @ x <= ub
        constraints = LinearConstraint(A, target, target)

        # Bounds: x_j >= 0, and we set an upper bound based on max target value
        max_presses = max(target_joltages) + 1
        bounds = Bounds(lb=0, ub=max_presses)

        # Integrality: all variables must be integers (1 = integer)
        integrality = np.ones(num_schematics, dtype=int)

        # Solve the ILP
        result = milp(
            c, constraints=constraints, bounds=bounds, integrality=integrality
        )

        if result.success:
            min_presses = int(round(result.fun))

        total_presses += min_presses

    return total_presses


# def main_part_two(problem_input: str) -> Any:
#     lines = problem_input.splitlines()
#     total_presses = 0

#     for i, line in enumerate(lines):
#         print(f"Processing line: {i+1} / {len(lines)}")
#         target_joltages = list(map(int, line.split(" ")[-1].strip("{}").split(",")))
#         schematics = [
#             tuple(map(int, schematic.strip("()").split(",")))
#             for schematic in line.split(" ")[1:-1]
#         ]
#         min_presses = float("inf")

#         formatted_schematics = []
#         for schematic in schematics:
#             formatted_schematic = [0 for _ in range(len(target_joltages))]
#             for idx in schematic:
#                 formatted_schematic[idx] = 1

#             formatted_schematics.append(formatted_schematic)

#         all_indices = {}
#         for indices in product(
#             *[
#                 range(max([joltage for joltage in target_joltages]))
#                 for _ in formatted_schematics
#             ]
#         ):
#             try:
#                 all_indices[sum(indices)].append(indices)
#             except KeyError:
#                 all_indices[sum(indices)] = [indices]

#         for key in all_indices.keys():
#             completed = False
#             for indices in all_indices[key]:
#                 calculated_schematics = [0 for _ in range(len(target_joltages))]
#                 for j, indice in enumerate(indices):
#                     for k, formatted_schematic in enumerate(formatted_schematics[j]):
#                         calculated_schematics[k] += formatted_schematic * indice

#                 if calculated_schematics == target_joltages:
#                     min_presses = sum(indices)
#                     completed = True

#             if completed is True:
#                 break

#         total_presses += min_presses

#     return total_presses
