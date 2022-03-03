"""
https://rosalind.info/problems/sset/
"""
from collections import Counter
from src.utils import io


def count_subsets(n):
    m = 1000000
    n_subsets = 1
    for _ in range(n):
        n_subsets = (n_subsets * 2) % m
    return [str(n_subsets)]


if __name__ == "__main__":

    data, filename = io.read_data("sset")
    # data = ["3"]
    solution = count_subsets(int(data[0]))
    # print(solution)
    io.write_data(solution=solution, filename=filename)
