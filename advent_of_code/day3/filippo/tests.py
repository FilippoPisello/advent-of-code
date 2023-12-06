from advent_of_code.day3.filippo.solution import (
    Number,
    extract_numbers_from_line,
    has_symbol,
)


def test_if_single_number_in_row_then_it_is_extracted():
    line = "617*......"
    number = extract_numbers_from_line(line)
    assert number[0].value == 617


def test_if_two_numbers_in_row_then_both_are_extracted():
    line = "467..114.."
    numbers = extract_numbers_from_line(line)
    assert numbers[0].value == 467
    assert numbers[1].value == 114


def test_if_line_has_no_number_then_nothing_is_returned():
    line = "...*......"
    numbers = extract_numbers_from_line(line)
    assert numbers == []


def test_number_starting_and_ending_position_in_line_is_stored():
    line = ".617*....1111.."
    numbers = extract_numbers_from_line(line)
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
        number = Number(10, 139)
        assert number.same_row_indexes == {138}

    def test_index_on_adjacent_rows_are_same_and_one_before_start(self):
        number = Number(10, 139)
        assert number.adjacent_row_indexes == {138, 139, 140}


class TestSymbolDetection:
    def test_if_row_contains_symbol_at_one_of_the_indexes_then_true(self):
        line = "617*......"
        assert has_symbol(line, {3})

    def test_if_index_matches_dot_then_false(self):
        line = "617*......"
        assert not has_symbol(line, {5})
