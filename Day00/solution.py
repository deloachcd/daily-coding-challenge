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
        return min([list_element, k-list_element])

    # In a language without "dynamic array"-like lists, cells can be implemented
    # as linked lists
    cells = [[] for i in range((k//2)+1)]
    for _, element in enumerate(lst):
        # TODO explain how this works in comments
        negative = element < 0
        distance = (-1 if negative else 1) * element // (-k if negative else k)
        reduced_element = abs(element) % k
        hash_cell = cells[simple_hash(reduced_element)]
        for recorded_distance in hash_cell:
            if distance + recorded_distance == 0:
                return True
        hash_cell.append(distance)

    return False
