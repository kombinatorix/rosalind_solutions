"""
https://rosalind.info/problems/rna/
"""
from src.utils import io

def convert_dna_to_rna(sequence):
    return [f'{sequence.replace("T","U")}']

if __name__ == "__main__":

    data, filename =  io.read_data("rna")
    solution = convert_dna_to_rna(data[0])
    io.write_data(solution=solution, filename=filename)