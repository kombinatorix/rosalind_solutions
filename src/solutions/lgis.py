"""
https://rosalind.info/problems/lgis/
"""
from src.utils.io import read_data, write_data


def lis(array):
    n = len(array)
    q = [0] * n  # q[i] contains the max length of sub seq. ending at array[i]
    p = [-1] * n  # p[i] contains predecessor of the sub seq. ending at array[i]

    for i in range(n):
        maxLen = 0
        for j in range(i):
            if array[i] > array[j]:
                if q[j] > maxLen:
                    maxLen = q[j]
                    p[i] = j

        q[i] = maxLen + 1

    idx = q.index(max(q))
    seq = []
    while idx != -1:
        seq = [array[idx]] + seq
        idx = p[idx]

    return seq


def longest_subsequences(sequence):
    sequence = list(map(lambda x: int(x), sequence.split(" ")))
    neg_seqence = [-el for el in sequence]
    s1 = " ".join([str(el) for el in lis(sequence)])
    s2 = " ".join([str(-1 * el) for el in lis(neg_seqence)])
    return [s1, s2]


if __name__ == "__main__":

    data, filename = read_data("lgis")
    solution = longest_subsequences(data[1])
    write_data(solution=solution, filename=filename)
