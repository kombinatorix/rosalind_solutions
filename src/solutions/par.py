"""
https://rosalind.info/problems/dna/
"""
from src.utils import io
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

    data, filename = io.read_data("par")
    # data = ["9", "7 2 3 5 14 6 1 3 9 4 8"]
    solution = partition(string_to_list_ints(data[1]))
    solution = [list_ints_to_string(solution)]
    # print(solution)
    io.write_data(solution=solution, filename=filename)
