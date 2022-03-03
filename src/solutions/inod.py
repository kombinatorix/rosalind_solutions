"""
https://rosalind.info/problems/inod/
"""
from collections import Counter
from src.utils import io


def compute_internal_nodes(n):
    return [str(n - 2)]


if __name__ == "__main__":

    data, filename = io.read_data("inod")
    solution = compute_internal_nodes(int(data[0]))
    io.write_data(solution=solution, filename=filename)
