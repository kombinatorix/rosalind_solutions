"""
https://rosalind.info/problems/dna/
"""
from collections import Counter
from src.utils import io

def count_symbols(sequence):
    counter = Counter(sequence)
    return [f'{counter["A"]} {counter["C"]} {counter["G"]} {counter["T"]}']

if __name__ == "__main__":

    data, filename =  io.read_data("dna")
    solution = count_symbols(data[0])
    io.write_data(solution=solution, filename=filename)