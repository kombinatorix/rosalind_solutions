"""
https://rosalind.info/problems/lexf/
"""
from src.utils.io import read_data, write_data
from itertools import combinations_with_replacement


def compute_kmers(alphabet, k):
    ordered_alphabet = alphabet.split()
    return ["".join(el) for el in combinations_with_replacement(ordered_alphabet, k)]


if __name__ == "__main__":

    data, filename = read_data("lexf")
    solution = compute_kmers(data[0], int(data[1]))
    write_data(solution=solution, filename=filename)
