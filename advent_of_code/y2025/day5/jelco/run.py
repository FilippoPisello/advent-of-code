"""Quick runner for the solution."""

from pathlib import Path
from solution import main_part_one, main_part_two

if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    problem_input = input_file.read_text()

    print("=== Part One ===")
    result_one = main_part_one(problem_input)
    print(f"Result: {result_one}")

    print("\n=== Part Two ===")
    result_two = main_part_two(problem_input)
    print(f"Result: {result_two}")
