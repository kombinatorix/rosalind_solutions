"""
https://rosalind.info/problems/lexv/
"""
from src.utils.io import read_data, write_data
from itertools import combinations_with_replacement


def compute_kmers(alphabet, k):
    ordered_alphabet = alphabet.split()
    strings = []
    for i in range(1, k + 1):
        strings += [
            "".join(el) for el in combinations_with_replacement(ordered_alphabet, i)
        ]
    return sorted(strings, key=lambda word: [ordered_alphabet.index(c) for c in word])


if __name__ == "__main__":

    data, filename = read_data("lexv")
    solution = compute_kmers(data[0], int(data[1]))
    write_data(solution=solution, filename=filename)
