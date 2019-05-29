from solution import generate_product_list


def test_generate_product_list():
    assert generate_product_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
