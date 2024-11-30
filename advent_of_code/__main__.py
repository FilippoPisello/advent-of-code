import argparse
from importlib import import_module

import pytest

from advent_of_code import MODULE_DIR
from advent_of_code.read_input import read_txt_input


def main():
    args = _parse_args()
    if args.create:
        _create_day_user_dir(args.day, args.user, args.year)
    elif args.test:
        run_tests(args.day, args.user, args.year)
    else:
        function_to_call = _derive_function_name(args.part)
        run_solution(args.day, args.user, args.year, function_to_call)


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Run your solution or tests for a day of the Advent of Code challenge."
    )
    parser.add_argument("day", type=int, help="The number of the day to run.")
    parser.add_argument("user", type=str, help="The user to run for.")
    parser.add_argument(
        "--test",
        "--tests",
        action="store_true",
        help="Run tests instead of the solution.",
        default=False,
    )
    parser.add_argument(
        "--part",
        type=int,
        help="Run only one part of the solution.",
        choices=[1, 2],
        default=None,
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create a new user directory.",
        default=False,
    )
    parser.add_argument(
        "--year",
        type=int,
        help="The edition you are working on.",
        default=2024,
    )
    return parser.parse_args()


def _create_day_user_dir(day: int, user: str, year: int) -> None:
    user_dir = MODULE_DIR / f"{year}/day{day}/{user}"
    user_dir.mkdir(parents=True, exist_ok=True)
    (user_dir / "solution.py").touch()
    (user_dir / "tests.py").touch()
    (user_dir / "input.txt").touch()
    file = open(user_dir / "solution.py", "w", encoding="utf-8")
    file.write(
        (
            "def main_part_one(problem_input: list[str]):\n"
            "    return\n"
            "\n"
            "def main_part_two(problem_input: list[str]):\n"
            "    return\n"
        )
    )
    file.close()


def _derive_function_name(part: int | None) -> str:
    if part is None:
        return "main"
    digitstr = {1: "one", 2: "two"}
    return f"main_part_{digitstr[part]}"


def run_solution(day: int, user: str, year: int, function: str) -> None:
    problem_input = read_txt_input(day, user, year)
    user_dir = ".".join(["advent_of_code", str(year), f"day{day}", user])
    solution_module = import_module(user_dir + ".solution")
    solution_function = getattr(solution_module, function)
    print(f"Running '{function}' for '{user}', day '{day}'...")
    result = solution_function(problem_input)
    print(result)


def run_tests(day: int, user: str, year: int) -> None:
    pytest.main([MODULE_DIR / f"{year}/day{day}/{user}/tests.py"])


if __name__ == "__main__":
    main()
