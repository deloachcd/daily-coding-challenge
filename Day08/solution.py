def largest_sum_non_adjacent(lst: list):
    def sum_from_index(i):
        rsum = lst[i]
        while i + 2 < len(lst):
            if i + 3 < len(lst):
                current, other = sum(lst[i + 2 : i + 5 : 2]), lst[i + 3]
                if current >= other:
                    # stay on current row
                    rsum += lst[i + 2]
                    i += 2
                else:
                    # switch rows
                    rsum += lst[i + 3]
                    i += 3
            else:
                rsum += lst[i + 2]
                i += 2
        return rsum

    return max(sum_from_index(0), sum_from_index(1))
