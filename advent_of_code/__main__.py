import argparse
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path

import pytest

from advent_of_code import MODULE_DIR, MODULE_NAME


@dataclass
class Folder:
    user: str
    day: int
    year: int

    @property
    def file_path(self) -> Path:
        """Return the path (e.g. 'advent_of_code/2023/day1/Foo')."""
        return MODULE_DIR / f"{self.year}/day{self.day}/{self.user}"

    @property
    def import_path(self) -> str:
        """Return the import path (e.g. 'advent_of_code.2023.day1.Foo')."""
        return ".".join([MODULE_NAME, str(self.year), f"day{self.day}", self.user])


def main():
    args = _parse_args()
    folder = Folder(args.user, args.day, args.year)
    if args.create:
        _create_day_user_files(folder.file_path)
        _write_solution_template(folder.file_path)
    elif args.test:
        pytest.main(folder.file_path / "tests.py")
    else:
        content = (folder.file_path / "input.txt").read_text()
        function_to_call = _derive_function_name(args.part)
        _run_solution(folder, function_to_call, content)


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


def _create_day_user_files(user_dir: Path) -> None:
    user_dir.mkdir(parents=True, exist_ok=True)
    for file_name in ["solution.py", "tests.py", "input.txt"]:
        (user_dir / file_name).touch()


def _write_solution_template(user_dir: Path) -> None:
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


def _run_solution(folder: Folder, function: str, problem_input: str) -> None:
    solution_module = import_module(folder.import_path + ".solution")
    solution_function = getattr(solution_module, function)
    print(f"Running '{function}' for '{folder.user}', day '{folder.day}'...")
    result = solution_function(problem_input)
    print(result)


if __name__ == "__main__":
    main()
