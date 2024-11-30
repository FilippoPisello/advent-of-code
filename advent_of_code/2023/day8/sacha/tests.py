from advent_of_code.day8.sacha.solution import input_to_dict, main


def test_instruction():
    data = ["RL", "", "FPF = (PTN, MPT)"]
    solution = "RL"
    dict, instruction = input_to_dict(data)
    assert instruction == solution


def test_dict():
    data = ["RL", "", "FPF = (PTN, MPT)"]
    solution = {"FPF": ["PTN", "MPT"]}
    dict, instruction = input_to_dict(data)
    assert dict == solution


def test_main_example():
    data = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]
    assert main(data) == 6
