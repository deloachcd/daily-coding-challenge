from solution import count_possibilities


def test_their_cases():
    assert count_possibilities('111') == 3


def test_my_cases():
    assert count_possibilities('11') == 2
    assert count_possibilities('27') == 1
    assert count_possibilities('261') == 2
