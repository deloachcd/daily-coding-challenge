from solution import largest_sum_non_adjacent


def test_their_cases():
    assert largest_sum_non_adjacent([2, 4, 6, 2, 5]) == 13
    assert largest_sum_non_adjacent([5, 1, 1, 5]) == 10


def test_my_cases():
    assert largest_sum_non_adjacent([5, 1, 1, 7, 1, 1, 5]) == 17
    assert largest_sum_non_adjacent([5, 1, 1, 7, 1, 5, 1]) == 17
    assert largest_sum_non_adjacent([5, 1, 1, 1, 7, 1, 1, 5]) == 18
    assert largest_sum_non_adjacent([1, 5, 1, 1, 7, 1, 1, 5]) == 17
