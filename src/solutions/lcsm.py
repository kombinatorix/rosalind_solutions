"""
https://rosalind.info/problems/lcsm/
"""
from src.utils import io


def compute_gc_content(genetic_strings):
    dna_strings = [el.gen_string for el in genetic_strings]

    molecules = ["A", "C", "G", "T"]
    previous_substrings = ["A", "C", "G", "T"]

    while True:
        potential_substrings = []
        for molecule in molecules:
            potential_substrings.extend([s + molecule for s in previous_substrings])
        tmp_previous_substrings = []
        for s in potential_substrings:
            for dna_string in dna_strings:
                if s not in dna_string:
                    break
            else:
                tmp_previous_substrings.append(s)
        if len(tmp_previous_substrings) == 0:
            break
        else:
            previous_substrings = tmp_previous_substrings
    return [previous_substrings[0]]


if __name__ == "__main__":

    data, filename = io.read_fasta("lcsm")
    solution = compute_gc_content(data)
    io.write_data(solution=solution, filename=filename)
