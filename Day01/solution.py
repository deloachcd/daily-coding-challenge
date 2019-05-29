from functools import reduce


def generate_product_list(lst):
    def prod(x, y):
        return x * y

    new_list = lst.copy()
    for i, _ in enumerate(lst):
        new_list[i] = reduce(prod, lst[:i] + lst[i+1:])

    return new_list
