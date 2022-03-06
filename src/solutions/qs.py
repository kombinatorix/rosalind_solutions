"""
https://rosalind.info/problems/qs/
"""
from src.utils.io import read_data, write_data
from src.utils.converter import string_to_list_ints, list_ints_to_string

# Todo: in place
def quicksort(seq):
    if len(seq) <= 1:
        return seq
    l = seq[0]
    left, middle, right = [], [], []
    for el in seq[1:]:
        if el < l:
            left.append(el)
        elif el == l:
            middle.append(el)
        else:
            right.append(el)
    return quicksort(left) + [l] + middle + quicksort(right)


if __name__ == "__main__":

    data, filename = read_data("qs")
    solution = quicksort(string_to_list_ints(data[1]))
    solution = [list_ints_to_string(solution)]
    write_data(solution=solution, filename=filename)
