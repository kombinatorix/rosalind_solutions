"""
https://rosalind.info/problems/iprb/
"""
from src.utils.io import read_data, write_data
from math import comb


def mendels_first_law(k, m, n):
    """
    k = homozygous dominant
    m = m are heterozygous
    n = homozygous recessive
    """
    number_of_indiv = k + m + n
    number_of_total_outcomes = comb(number_of_indiv, 2)
    dominant_combinations = (
        comb(k, 2) + k * m + k * n + 1 / 2 * m * n + 3 / 4 * comb(m, 2)
    )

    return [f"{dominant_combinations / number_of_total_outcomes:.5f}"]


if __name__ == "__main__":

    data, filename = read_data("iprb")
    solution = mendels_first_law(*map(lambda x: int(x), data[0].split(" ")))
    write_data(solution=solution, filename=filename)
