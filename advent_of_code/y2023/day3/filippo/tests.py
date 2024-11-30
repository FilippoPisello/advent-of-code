from advent_of_code.day3.filippo.solution import (
    Asterisk,
    Number,
    extract_asterisks_from_line,
    has_symbol,
    main_part_one,
    main_part_two,
)


def test_if_single_number_in_row_then_it_is_extracted():
    line = "617*......"
    number = Number.from_line(line)
    assert number[0].int_value == 617


def test_if_two_numbers_in_row_then_both_are_extracted():
    line = "467..114.."
    numbers = Number.from_line(line)
    assert numbers[0].int_value == 467
    assert numbers[1].int_value == 114


def test_if_line_has_no_number_then_nothing_is_returned():
    line = "...*......"
    numbers = Number.from_line(line)
    assert numbers == []


def test_number_starting_and_ending_position_in_line_is_stored():
    line = ".617*....1111.."
    numbers = Number.from_line(line)
    assert numbers[0].starting_index == 1
    assert numbers[0].ending_index == 3
    assert numbers[1].starting_index == 9
    assert numbers[1].ending_index == 12


class TestNumberStartOfTheRow:
    def test_indexes_on_the_same_row_is_only_one_after_ending(self):
        number = Number(10, 0)
        assert number.same_row_indexes == {2}

    def test_index_on_adjacent_rows_are_same_and_one_after_ending(self):
        number = Number(10, 0)
        assert number.adjacent_row_indexes == {0, 1, 2}


class TestNumberIsCenterOfTheRow:
    def test_indexes_on_the_same_row_are_before_and_after(self):
        number = Number(10, 1)
        assert number.same_row_indexes == {0, 3}

    def test_index_on_adjacent_rows_are_same_and_before_and_after(self):
        number = Number(10, 1)
        assert number.adjacent_row_indexes == {0, 1, 2, 3}


class TestNumberIsEndOfRow:
    def test_indexes_on_the_same_row_is_only_one_before_start(self):
        number = Number(10, 138)
        assert number.same_row_indexes == {137}

    def test_index_on_adjacent_rows_are_same_and_one_before_start(self):
        number = Number(10, 138)
        assert number.adjacent_row_indexes == {137, 138, 139}


class TestSymbolDetection:
    def test_if_row_contains_symbol_at_one_of_the_indexes_then_true(self):
        line = "617*......"
        assert has_symbol(line, {3})

    def test_if_index_matches_dot_then_false(self):
        line = "617*......"
        assert not has_symbol(line, {5})


def test_example_part_one():
    problem_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert main_part_one(problem_input) == 4361


def test_if_two_asterisks_in_row_then_both_are_extracted():
    line = "...*....*.."
    asterisks = Asterisk.from_line(line)
    assert asterisks[0].starting_index == 3
    assert asterisks[1].starting_index == 8


def test_example_part_two():
    problem_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert main_part_two(problem_input) == 467835
