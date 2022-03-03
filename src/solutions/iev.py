"""
https://rosalind.info/problems/iev/
"""
from collections import Counter
from src.utils import io
from math import comb

# def number_outcome(k,m,n):
#    return 2*k+m, m+2*n # dominant, recessive


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

    # print(sum([(idx + 1) * el * pr_x[idx] for idx, el in enumerate(population)]))

    # return [f"{dominant_combinations / number_of_total_outcomes:.5f}"]


if __name__ == "__main__":

    data, filename = io.read_data("iev")
    # data = ["1 0 0 1 0 1"]
    solution = compute_expected_offspring(map(lambda x: int(x), data[0].split(" ")))
    # print(solution)
    io.write_data(solution=solution, filename=filename)
