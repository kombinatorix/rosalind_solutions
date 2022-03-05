"""
https://rosalind.info/problems/par3/
"""
from src.utils import io
from src.utils.converter import string_to_list_ints, list_ints_to_string

# Todo: in place
def partition(seq):
    l = seq[0]
    left, middle, right = [], [], []
    for el in seq[1:]:
        if el < l:
            left.append(el)
        elif el == l:
            middle.append(el)
        else:
            right.append(el)
    return left + [l] + middle + right


if __name__ == "__main__":

    data, filename = io.read_data("par3")
    # data = ["9", "4 5 6 4 1 2 5 7 4"]
    solution = partition(string_to_list_ints(data[1]))
    solution = [list_ints_to_string(solution)]
    # print(solution)
    io.write_data(solution=solution, filename=filename)
