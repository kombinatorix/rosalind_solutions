"""
https://rosalind.info/problems/sign/
"""
from src.utils.io import read_data, write_data
from itertools import permutations, product


def compute_signed_permutations(n):
    perms = list(permutations(range(1, n + 1)))
    sign = list(product([1, -1], repeat=n))
    signed_perms = []
    for s in sign:
        signed_perms += [
            " ".join([str(el1 * el2) for el1, el2 in zip(s, p)]) for p in perms
        ]
    return [str(len(signed_perms))] + signed_perms


if __name__ == "__main__":

    data, filename = read_data("sign")
    solution = compute_signed_permutations(int(data[0]))
    write_data(solution=solution, filename=filename)
