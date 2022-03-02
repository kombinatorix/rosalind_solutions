"""
https://rosalind.info/problems/iprb/
"""
from collections import Counter
from src.utils import io
from math import comb

# def number_outcome(k,m,n):
#    return 2*k+m, m+2*n # dominant, recessive


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

    data, filename = io.read_data("iprb")
    # data = ["2 2 2"]
    solution = mendels_first_law(*map(lambda x: int(x), data[0].split(" ")))
    io.write_data(solution=solution, filename=filename)
