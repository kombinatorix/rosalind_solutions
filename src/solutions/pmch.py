"""
https://rosalind.info/problems/pmch/
"""
from collections import Counter
from src.utils.io import read_fasta, write_data
import math


def compute_number_of_perfect_matchings(genetic_string):
    counter = Counter(genetic_string.gen_string)
    number_of_matchings = math.factorial(counter["A"]) * math.factorial(counter["C"])
    return [f"{number_of_matchings}"]


if __name__ == "__main__":

    data, filename = read_fasta("pmch")
    solution = compute_number_of_perfect_matchings(data[0])
    write_data(solution=solution, filename=filename)
