# Advent of Code

Store the Advent of Code solutions of the analysts of Picnic France and beyond! Provides a couple of CLI functionalities to make life just a bit simpler to jump right into the puzzles!

## How to use

### Installing the project
This project uses poetry, to install what is needed to run solutions run:
```
poetry install --sync
```
If you want to run tests or develop:
```
poetry install --sync --all-extras
```

> [!NOTE]
> From now onwards, you expected to run any `python` command within your poetry environment. This means either activating your poetry shell once by running `poetry shell` or by prepending each command with `poetry run`, so that when you see `python ...` you should run `poetry run python ...`.

> [!IMPORTANT]
> In principle this project should require no extra dependencies. If you want top add one to use in one of your solutions, make sure to install it by creating a dependency group under your name, so like `poetry add <your-dependency> --group <your-name>`. You can check what "current edition" means by looking at the value of `CURRENT_EDITION` variable in `advent_of_code/__init__.py`.

### Working on your solution

#### Creating your files
Create the files to host your solution with:
```bash
python -m advent_of_code <day-number> <your_name> --create
```
Ta-da! The script has created four you a folder `advent_of_code/y<year>/day<day>/<your-name>/` containing files for your input, solution and tests.

> [!TIP]
> By default it is assumed that you are working on the current edition, if you are instead on the puzzles of a different year, add the `--year` option like `python -m advent_of_code <day-number> <your_name> --create --year 2022`. You can check what "current edition" means by looking at the value of `CURRENT_EDITION` variable in `advent_of_code/__init__.py`.

#### Working on your solution
To get into the action:
- Copy-paste the content of your daily input into the corresponding file like `advent_of_code/y<year>/day<day>/<your-name>/input.txt`.
- Write your solution either by:
  - Tackling the two parts individually, thus filling in separately `main_part_one` and `main_part_two`.
  - Doing all in one step, in that case you want to uncomment the `main` function just below.

> [!NOTE]
> Your solution function(s) should:
> - Accept a `problem_input` argument, containing the entire raw content of your input file as a single `str`.
> - Return whatever output you get to.

#### Running your solution

You can easily run your solution and get your output directly in the terminal.
If you sticked to the two-parts approach, run:
```bash
python -m advent_of_code <day-number> <your_name> --part <1 or 2>
```

In case you opted for a single `main` function, run instead:
```bash
python -m advent_of_code <day-number> <your_name>
```

> [!NOTE]
> If you are solving for a different year, also pass `--year 2022`

#### Testing

You can run your tests as follows:

```bash
python -m advent_of_code <day-number> <your_name> --test
```

> [!NOTE]
> If you are solving for a different year, also pass `--year 2022`
