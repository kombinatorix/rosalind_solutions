"""
https://rosalind.info/problems/grph/
"""
from src.utils import io
from itertools import combinations


def compute_overlap_graph(genetic_strings, k):
    return [
        f"{el1.name} {el2.name}"
        for el1, el2 in combinations(genetic_strings, 2)
        if el1.overlap_k(el2, k)
    ]


if __name__ == "__main__":

    data, filename = io.read_fasta("grph")
    # data = [
    #    ">Rosalind_0498",
    #    "AAATAAA",
    #    ">Rosalind_2391",
    #    "AAATTTT",
    #    ">Rosalind_2323",
    #    "TTTTCCC",
    #    ">Rosalind_0442",
    #    "AAATCCC",
    #    ">Rosalind_5013",
    #    "GGGTGGG",
    # ]
    # solution = compute_overlap_3_graph(io.data_to_genetic_string(data), k=3)
    solution = compute_overlap_graph(data, k=3)
    io.write_data(solution=solution, filename=filename)
