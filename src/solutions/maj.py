"""
https://rosalind.info/problems/maj/
"""
from collections import Counter
from src.utils.io import read_data, write_data


def empty_list():
    return []


def majority_degree(info, sequences):
    n_half = int(info.split(" ")[1]) / 2
    maj_list = []
    for seq in sequences:
        int_seq = list(map(lambda x: int(x), seq.split(" ")))
        tmp_set = {}
        for key, value in Counter(int_seq).items():
            if value > n_half:
                maj_list.append(str(key))
                break
        else:
            maj_list.append("-1")
    return [" ".join(maj_list)]


if __name__ == "__main__":

    data, filename = read_data("maj")
    solution = majority_degree(data[0], data[1:])
    write_data(solution=solution, filename=filename)
