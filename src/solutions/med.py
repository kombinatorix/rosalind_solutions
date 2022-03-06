"""
https://rosalind.info/problems/med/
"""
from collections import Counter
from src.utils.io import read_data, write_data
from src.utils.converter import string_to_list_ints


def get_k_smallest(sequence, k):
    counter = dict(Counter(sequence))
    sum = 0
    for idx in sorted(counter.keys()):
        sum += counter[idx]
        if sum >= k:
            return idx


if __name__ == "__main__":

    data, filename = read_data("med")
    solution = [str(get_k_smallest(string_to_list_ints(data[1]), int(data[2])))]
    write_data(solution=solution, filename=filename)
