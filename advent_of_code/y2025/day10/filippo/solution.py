"""Solution for day 10 of Advent of Code 2025, by filippo."""

from typing import Any


def main_part_one(problem_input: str) -> Any:
    counter = 0
    for config in problem_input.splitlines():
        end_state = config[1:].split("]")[0]
        buttons = parse_buttons(config)

        config_counter = 0
        paths = [["." * len(end_state)]]
        while end_state not in (st[-1] for st in paths):
            new_paths = []
            config_counter += 1
            for path in paths:
                current_state = path[-1]
                for button in buttons:
                    new_state = apply_button(current_state, button)
                    # No point in trying to pass again by a previously
                    # covered state
                    if new_state in path:
                        continue
                    new_paths.append(path + [new_state])
            paths = new_paths

        counter += config_counter

    return counter


def parse_buttons(config: str) -> set[tuple[int, ...]]:
    output = set()
    relevant_characters = config[config.index("(") : config.index("{")]
    simplified_characters = relevant_characters.replace("(", "").replace(")", "")
    for button in simplified_characters.split(" "):
        if button:
            key = tuple(map(int, button.split(",")))
            output.add(key)
    return output


def apply_button(state: str, button: tuple[int, ...]) -> str:
    _map = {"#": ".", ".": "#"}
    state_list = list(state)
    for index in button:
        state_list[index] = _map[state_list[index]]
    return "".join(state_list)


def main_part_two(problem_input: str) -> Any:
    counter = 0
    for machine_number, config in enumerate(problem_input.splitlines(), start=1):
        print(machine_number)
        end_joltage = parse_joltage(config)
        buttons = parse_buttons(config)

        config_counter = 0
        states = {tuple(0 for _ in end_joltage)}
        passed_joltages = states.copy()
        while end_joltage not in states:
            new_states: set[tuple[int, ...]] = set()
            config_counter += 1
            print(f"Counter {config_counter},{len(states)} states")
            for state in states:
                for button in buttons:
                    new_joltage = apply_button_on_joltage(state, button)
                    # No point in trying to pass again by a previously
                    # covered state
                    if joltage_beyond_target(new_joltage, end_joltage):
                        continue
                    if new_joltage in passed_joltages:
                        continue
                    if any(
                        joltage_pareto_inferior(new_joltage, pj)
                        for pj in passed_joltages
                    ):
                        continue
                    # voltages
                    new_states.add(new_joltage)
                    passed_joltages.add(new_joltage)
            states = new_states

        counter += config_counter

    return counter


def parse_joltage(config: str) -> tuple[int, ...]:
    relevant_characters = config[config.index("{") : config.index("}")]
    simplified_characters = relevant_characters.replace("{", "").replace("}", "")
    return tuple(map(int, simplified_characters.split(",")))


def apply_button_on_joltage(
    joltage: tuple[int, ...], button: tuple[int, ...]
) -> tuple[int, ...]:
    new_joltage = list(joltage)
    for index in button:
        new_joltage[index] += 1
    return tuple(new_joltage)


def joltage_beyond_target(joltage: tuple[int, ...], target: tuple[int, ...]) -> bool:
    return any(j > t for j, t in zip(joltage, target))


def joltage_pareto_inferior(
    joltage: tuple[int, ...], benchmark: tuple[int, ...]
) -> bool:
    return all(j <= b for j, b in zip(joltage, benchmark))


# def main(problem_input: str) -> Any:
#    return
