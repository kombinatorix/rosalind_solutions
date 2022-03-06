"""
https://rosalind.info/problems/pdst/
"""
from src.utils.io import read_fasta, write_data


def hamming_distance(sequence_1, sequence_2):
    return sum([1 if el_1 != el_2 else 0 for el_1, el_2 in zip(sequence_1, sequence_2)])


def compute_gc_content(genetic_strings):
    l = len(genetic_strings[0].gen_string)

    return [
        " ".join(
            [
                f"{hamming_distance(g1.gen_string, g2.gen_string) / l:.5f}"
                for g2 in genetic_strings
            ]
        )
        for g1 in genetic_strings
    ]


if __name__ == "__main__":

    data, filename = read_fasta("pdst")
    solution = compute_gc_content(data)
    write_data(solution=solution, filename=filename)
