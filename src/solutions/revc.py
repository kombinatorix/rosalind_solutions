"""
https://rosalind.info/problems/revc/
"""
from src.utils.io import read_data, write_data
from src.utils.mappings import dna_complements


def complement_dna(sequence):
    complement = [dna_complements[el] for el in sequence[::-1]]
    return [f'{"".join(complement)}']


if __name__ == "__main__":

    data, filename = read_data("revc")
    solution = complement_dna(data[0])
    write_data(solution=solution, filename=filename)
