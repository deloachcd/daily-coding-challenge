from solution import linear_solution


def test_linear_solution_positive_integers():
    assert linear_solution([1, 2, 3], 1) is False
    assert linear_solution([1, 2, 3], 5) is True
    assert linear_solution([10, 15, 3, 7], 17) is True
    assert linear_solution([10, 15, 3, 7], 10) is True
    assert linear_solution([10, 15, 3, 7], 7) is False
