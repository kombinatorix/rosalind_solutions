"""
https://rosalind.info/problems/inod/
"""
from src.utils.io import read_data, write_data


def compute_internal_nodes(n):
    return [str(n - 2)]


if __name__ == "__main__":

    data, filename = read_data("inod")
    solution = compute_internal_nodes(int(data[0]))
    write_data(solution=solution, filename=filename)
