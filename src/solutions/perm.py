"""
https://rosalind.info/problems/perm/
"""
from src.utils.io import read_data, write_data
from itertools import permutations


def compute_permutations(n):
    n_str = [str(el) for el in range(1, int(n) + 1)]
    perms = [" ".join(perm) for perm in permutations(n_str)]
    return [str(len(perms))] + perms


if __name__ == "__main__":

    data, filename = read_data("perm")
    solution = compute_permutations(data[0])
    write_data(solution=solution, filename=filename)
