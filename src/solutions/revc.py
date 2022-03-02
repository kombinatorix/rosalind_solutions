"""
https://rosalind.info/problems/revc/
"""
from collections import Counter
from src.utils import io, mappings

def complement_dna(sequence):
    complement = [mappings.dna_complements[el] for el in sequence[::-1]]
    return [f'{"".join(complement)}']

if __name__ == "__main__":
    data, filename =  io.read_data("revc")
    solution = complement_dna(data[0])
    io.write_data(solution=solution, filename=filename)