"""
https://rosalind.info/problems/mrna/
"""
from src.utils import io
from src.utils.mappings import inverse_rna_codon_table
from collections import defaultdict


def inferring_mrna_from_prot(sequence):
    modulo = 1000000
    prod = 1
    for el in sequence:
        prod *= len(inverse_rna_codon_table[el])
        prod = prod % modulo
    return [str((prod * len(inverse_rna_codon_table["Stop"])) % modulo)]


if __name__ == "__main__":

    data, filename = io.read_data("mrna")
    # data = ["MA"]
    solution = inferring_mrna_from_prot(data[0])
    io.write_data(solution=solution, filename=filename)
