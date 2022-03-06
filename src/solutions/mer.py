"""
https://rosalind.info/problems/mer/
"""
from src.utils.io import read_data, write_data


def merge(seq1, seq2):
    int_seq1 = list(map(lambda x: int(x), seq1.split(" ")))
    int_seq2 = list(map(lambda x: int(x), seq2.split(" ")))
    left_idx, right_idx = 0, 0
    ordered_list = []
    while left_idx < len(int_seq1) and right_idx < len(int_seq2):
        if int_seq1[left_idx] <= int_seq2[right_idx]:
            ordered_list.append(str(int_seq1[left_idx]))
            left_idx += 1
        else:
            ordered_list.append(str(int_seq2[right_idx]))
            right_idx += 1
    if left_idx < len(int_seq1):
        ordered_list += [str(el) for el in int_seq1[left_idx:]]
    else:
        ordered_list += [str(el) for el in int_seq2[right_idx:]]

    return [" ".join(ordered_list)]


if __name__ == "__main__":

    data, filename = read_data("mer")
    solution = merge(data[1], data[3])
    write_data(solution=solution, filename=filename)
