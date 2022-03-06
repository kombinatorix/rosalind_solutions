"""
https://rosalind.info/problems/rna/
"""
from src.utils.io import read_data, write_data


def convert_dna_to_rna(sequence):
    return [f'{sequence.replace("T","U")}']


if __name__ == "__main__":

    data, filename = read_data("rna")
    solution = convert_dna_to_rna(data[0])
    write_data(solution=solution, filename=filename)
