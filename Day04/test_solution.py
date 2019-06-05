from solution import cons, car, cdr


def test_their_cases():
    my_pair = cons(3, 4)
    assert car(my_pair) == 3
    assert cdr(my_pair) == 4
