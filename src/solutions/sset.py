"""
https://rosalind.info/problems/sset/
"""
from src.utils.io import read_data, write_data


def count_subsets(n):
    modulo = 1_000_000
    n_subsets = 1
    for _ in range(n):
        n_subsets = (n_subsets * 2) % modulo
    return [str(n_subsets)]


if __name__ == "__main__":

    data, filename = read_data("sset")
    solution = count_subsets(int(data[0]))
    write_data(solution=solution, filename=filename)
