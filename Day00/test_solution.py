from solution import linear_solution


def test_linear_solution_positives_only():
    assert linear_solution([1, 2, 3], 1) is False
    assert linear_solution([1, 2, 3], 5) is True
    assert linear_solution([10, 15, 3, 7], 17) is True
    assert linear_solution([10, 15, 3, 7], 10) is True
    assert linear_solution([10, 15, 3, 7], 7) is False


def test_linear_solution_with_negatives():
    # TODO write more tests here
    assert linear_solution([-18, 15, 3, 35], 17) is True
