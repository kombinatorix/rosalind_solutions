"""
https://rosalind.info/problems/cons/
"""
from typing import Counter
from src.utils import io


def compute_consensus_string(genetic_strings):
    strings = [el.gen_string for el in genetic_strings]
    consensus_list = []
    nucleobase_dict = {
        "A": [],
        "C": [],
        "G": [],
        "T": [],
    }
    for cut in zip(*strings):
        counter = Counter(cut)
        for key in ["A", "C", "G", "T"]:
            if key in counter.keys():
                nucleobase_dict[key].append(str(counter[key]))
            else:
                nucleobase_dict[key].append("0")
        consensus_list.append(max(counter, key=counter.get))
    return ["".join(consensus_list)] + [
        f"{el}: {' '.join(nucleobase_dict[el])}" for el in ["A", "C", "G", "T"]
    ]


if __name__ == "__main__":

    data, filename = io.read_fasta("cons")
    solution = compute_consensus_string(data)
    print(solution)
    io.write_data(solution=solution, filename=filename)
