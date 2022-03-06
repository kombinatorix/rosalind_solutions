"""
https://rosalind.info/problems/grph/
"""
from src.utils.io import read_fasta, write_data
from itertools import combinations


def compute_overlap_graph(genetic_strings, k):
    return [
        f"{el1.name} {el2.name}"
        for el1, el2 in combinations(genetic_strings, 2)
        if el1.overlap_k(el2, k)
    ]


if __name__ == "__main__":

    data, filename = read_fasta("grph")
    solution = compute_overlap_graph(data, k=3)
    write_data(solution=solution, filename=filename)
