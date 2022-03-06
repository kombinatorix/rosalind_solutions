"""
https://rosalind.info/problems/iev/
"""
from src.utils.io import read_data, write_data
from math import comb


def compute_expected_offspring(population):
    """
    1. AA-AA
    2. AA-Aa
    3. AA-aa
    4. Aa-Aa
    5. Aa-aa
    6. aa-aa
    """
    pr_x_AA = [1, 3 / 4, 0, 1 / 4, 0, 0]
    pr_x_Aa = [0, 1 / 4, 1, 1 / 2, 1 / 2, 0]

    return [
        str(
            sum(
                [
                    2 * (el1 + el2) * p
                    for el1, el2, p in zip(pr_x_AA, pr_x_Aa, population)
                ]
            )
        )
    ]


if __name__ == "__main__":

    data, filename = read_data("iev")
    solution = compute_expected_offspring(map(lambda x: int(x), data[0].split(" ")))
    write_data(solution=solution, filename=filename)
