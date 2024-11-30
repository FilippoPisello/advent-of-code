from advent_of_code.day3.david.solution import extract_numbers_from_line,extract_symbols_from_row


def test_if_single_number_in_row_then_it_is_extracted():
    line = "617*......"
    number = extract_numbers_from_line(line)
    assert number[0].value == "617"


def test_if_two_numbers_in_row_then_both_are_extracted():
    line = "467..114.."
    numbers = extract_numbers_from_line(line)
    assert numbers[0].value == "467"
    assert numbers[1].value == "114"


def test_if_line_has_no_number_then_nothing_is_returned():
    line = "...*......"
    numbers = extract_numbers_from_line(line)
    assert numbers == []


def test_number_starting_and_ending_position_in_line_is_stored():
    line = ".617*......"
    numbers = extract_numbers_from_line(line)
    assert numbers[0].starting_index == 0
    assert numbers[0].ending_index == 2

def test_if_two_symbols_in_row_then_both_are_extracted():
    line = "46*..11+.."
    numbers = extract_symbols_from_row(line)
    assert numbers[0].value == "*"
    assert numbers[1].value == "+"
    assert numbers[0].starting_index == '2'