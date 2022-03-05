"""
https://rosalind.info/problems/med/
"""
from collections import Counter
from src.utils import io
from src.utils.converter import string_to_list_ints


def get_k_smallest(sequence, k):
    counter = dict(Counter(sequence))
    sum = 0
    for idx in sorted(counter.keys()):
        sum += counter[idx]
        if sum >= k:
            return idx


if __name__ == "__main__":

    data, filename = io.read_data("med")
    # data = [
    #    "11",
    #    "2 36 5 21 8 13 11 20 5 4 1",
    #    "8",
    # ]
    solution = [str(get_k_smallest(string_to_list_ints(data[1]), int(data[2])))]
    # print(solution)
    io.write_data(solution=solution, filename=filename)
