"""
https://rosalind.info/problems/par/
"""
from src.utils.io import read_data, write_data
from src.utils.converter import string_to_list_ints, list_ints_to_string

# Todo: in place
def partition(seq):
    l = seq[0]
    left, right = [], []
    for el in seq[1:]:
        if el <= l:
            left.append(el)
        else:
            right.append(el)
    return left + [l] + right


if __name__ == "__main__":

    data, filename = read_data("par")
    solution = partition(string_to_list_ints(data[1]))
    solution = [list_ints_to_string(solution)]
    write_data(solution=solution, filename=filename)
