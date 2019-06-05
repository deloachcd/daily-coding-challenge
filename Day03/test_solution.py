from solution import missing_element


def test_their_cases():
    assert missing_element([1, 2, 0]) == 3
    assert missing_element([3, 4, -1, 1]) == 2

def test_my_cases():
    assert missing_element([3, 4, 3, 1]) == 2
    assert missing_element([4, 5, -1, 1, 3]) == 2
    assert missing_element([4, 2, -1, 1, 5]) == 3
    assert missing_element([3, 5, 4, 3, 6, 1, 7]) == 2

