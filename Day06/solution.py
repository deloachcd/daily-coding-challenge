def count_possibilities(message: str):
    possibilities = []

    def inner_count(msg_list: list):
        if all([type(item) is str for item in msg_list]):
            decoding = "".join(msg_list)
            if decoding not in possibilities:
                possibilities.append(decoding)
        for i, item in enumerate(msg_list):
            if type(item) is str:
                continue
            elif type(item) is int:
                new_permutation = msg_list[:i]
                if  (len(msg_list[i:i+2]) == 2 and type(msg_list[i+1]) is int):
                    potential_value = int("{}{}".format(msg_list[i], msg_list[i+1]))
                    if potential_value > 0 and potential_value < 27:
                        new_permutation += chr(int("{}{}".format(msg_list[i], msg_list[i+1]))
                                               + ord('a') - 1)
                        new_permutation += msg_list[i+2:]
                        inner_count(new_permutation)
                else:
                    new_permutation += chr(item + ord('a') - 1)
                    new_permutation += msg_list[i+1:]
                    inner_count(new_permutation)

    inner_count([int(num) for num in message])
    return len(possibilities)
