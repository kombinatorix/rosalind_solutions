
"""
https://rosalind.info/problems/hamm/
"""
from collections import Counter
from src.utils import io, mappings

def hamming_distance(sequence_1, sequence_2):
    return [str(sum([1 if el_1 != el_2 else 0 for el_1,el_2 in zip(sequence_1,sequence_2)]))]


if __name__ == "__main__":
    data, filename =  io.read_data("hamm")
    solution = hamming_distance(data[0], data[1])
    io.write_data(solution=solution, filename=filename)