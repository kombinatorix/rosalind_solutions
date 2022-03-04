"""
https://rosalind.info/problems/maj/
"""
from collections import Counter
from src.utils import io


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

    data, filename = io.read_data("maj")
    # data = [
    #    "4 8",
    #    "5 5 5 5 5 5 5 5",
    #    "8 7 7 7 1 7 3 7",
    #    "7 1 6 5 10 100 1000 1",
    #    "5 1 6 7 1 1 10 1",
    # ]
    solution = majority_degree(data[0], data[1:])
    # print(solution)
    io.write_data(solution=solution, filename=filename)
