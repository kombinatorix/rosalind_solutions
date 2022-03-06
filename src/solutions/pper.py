"""
https://rosalind.info/problems/pper/
"""
from src.utils.io import read_data, write_data


def compute_number_partial_permutations(n, k):
    m = 1000000
    n_k = 1
    for i in range(n - k + 1, n + 1):
        n_k = (n_k * i) % m

    return [str(n_k)]


if __name__ == "__main__":
    data, filename = read_data("pper")
    solution = compute_number_partial_permutations(
        *map(lambda x: int(x), data[0].split(" "))
    )
    write_data(solution=solution, filename=filename)
