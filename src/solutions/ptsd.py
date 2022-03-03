"""
https://rosalind.info/problems/pdst/
"""
from src.utils import io


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

    data, filename = io.read_fasta("pdst")
    # data = [
    #    ">Rosalind_9499",
    #    "TTTCCATTTA",
    #    ">Rosalind_0942",
    #    "GATTCATTTC",
    #    ">Rosalind_6568",
    #    "TTTCCATTTT",
    #    ">Rosalind_1833",
    #    "GTTCCATTTA",
    # ]
    # data = io.data_to_genetic_string(data)
    solution = compute_gc_content(data)
    io.write_data(solution=solution, filename=filename)
