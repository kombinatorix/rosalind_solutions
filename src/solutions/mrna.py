"""
https://rosalind.info/problems/mrna/
"""
from src.utils.io import read_data, write_data
from src.utils.mappings import inverse_rna_codon_table
from collections import defaultdict


def inferring_mrna_from_prot(sequence):
    modulo = 1_000_000
    prod = 1
    for el in sequence:
        prod *= len(inverse_rna_codon_table[el])
        prod = prod % modulo
    return [str((prod * len(inverse_rna_codon_table["Stop"])) % modulo)]


if __name__ == "__main__":

    data, filename = read_data("mrna")
    solution = inferring_mrna_from_prot(data[0])
    write_data(solution=solution, filename=filename)
