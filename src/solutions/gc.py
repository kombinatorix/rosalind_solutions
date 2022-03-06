"""
https://rosalind.info/problems/gc/
"""
from src.utils.io import read_fasta, write_data


def compute_gc_content(genetic_strings):
    name, percentage = sorted(
        [(el.name, el.calculate_percentage_of(["G", "C"])) for el in genetic_strings],
        key=lambda x: x[1],
    )[-1]
    return [name, f"{percentage:.6f}"]


if __name__ == "__main__":

    data, filename = read_fasta("gc")
    solution = compute_gc_content(data)
    write_data(solution=solution, filename=filename)
