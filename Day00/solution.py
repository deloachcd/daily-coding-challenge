def naive_solution(lst, k):
    # Runtime complexity: n^2
    for position, element in enumerate(lst):
        complement = k - element
        if complement in lst[position+1:]:
            return True
    return False

def linear_solution(lst, k, **kwargs):
    # This is a linear time solution - it uses a hashing function and a table to
    # determine if there are two elements in lst which sum to k in linear time
    def simple_hash(list_element):
        # This 'simple' hash function supports lists of positive numbers
        return min([list_element, k-list_element])

    # If two numbers 'hit' the same 'box' (hash to the same index in the table),
    # they sum to k
    hitboxes = [False for i in range((k//2)+1)]
    for _, element in enumerate(lst):
        if element >= 0 and element <= k:
            elmnt_hash = simple_hash(element)
            if 'DEBUG' in kwargs:
                print("{} -> {}".format(element, elmnt_hash))
            if hitboxes[elmnt_hash]:
                return True
            else:
                hitboxes[elmnt_hash] = True
    return False
