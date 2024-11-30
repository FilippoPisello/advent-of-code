from advent_of_code.day11.filippo.solution import (
    Galaxy,
    _parse_galaxies,
    _sum_shortest_distances,
    main_part_one,
)


class TestDistanceCalculation:
    @staticmethod
    def test_with_no_empty_rows_or_columns_distance_is_coordinates_delta():
        galaxy_1 = Galaxy(1, 1)
        galaxy_2 = Galaxy(2, 3)
        assert galaxy_1.distance(galaxy_2, {}, {}) == 3

    @staticmethod
    def test_with_empty_row_in_between_add_expansion_coefficient():
        galaxy_1 = Galaxy(1, 1)
        galaxy_2 = Galaxy(2, 3)
        Galaxy.EXPANSION_COEFFICIENT = 1
        assert galaxy_1.distance(galaxy_2, {2}, {}) == 4


def test_parse_galaxy_from_line():
    lines = [
        "....#........",
        ".........#...",
    ]
    assert _parse_galaxies(lines) == [Galaxy(4, 0), Galaxy(9, 1)]


def test_example_part_one():
    problem_input = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]
    assert main_part_one(problem_input) == 374
