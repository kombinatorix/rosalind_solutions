"""
https://rosalind.info/problems/pper/
"""
from collections import Counter
from src.utils import io


def compute_number_partial_permutations(n, k):
    m = 1000000
    n_k = 1
    for i in range(n - k + 1, n + 1):
        n_k = (n_k * i) % m

    return [str(n_k)]


if __name__ == "__main__":
    data, filename = io.read_data("pper")
    # data = ["21 7"]
    solution = compute_number_partial_permutations(
        *map(lambda x: int(x), data[0].split(" "))
    )
    # print(solution)
    io.write_data(solution=solution, filename=filename)
