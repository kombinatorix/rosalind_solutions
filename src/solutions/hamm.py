"""
https://rosalind.info/problems/hamm/
"""
from src.utils.io import read_data, write_data


def hamming_distance(sequence_1, sequence_2):
    return [
        str(
            sum(
                [1 if el_1 != el_2 else 0 for el_1, el_2 in zip(sequence_1, sequence_2)]
            )
        )
    ]


if __name__ == "__main__":
    data, filename = read_data("hamm")
    solution = hamming_distance(data[0], data[1])
    write_data(solution=solution, filename=filename)
