"""
https://rosalind.info/problems/ms/
"""
from heapq import merge
from src.utils import io
from functools import reduce


def ms(sq):
    new_seq = [[el] for el in sq]
    while len(new_seq) > 1:
        tmp_seq = []
        for i in range(0, len(new_seq), 2):
            tmp_seq.append(merge(new_seq[i], new_seq[i + 1]))
        new_seq = tmp_seq
    return new_seq[0]


def merge_sort(sequence):
    numbers = list(map(lambda x: int(x), sequence.split(" ")))
    bin_string = bin(len(numbers))
    reversed_bin_string = bin_string.split("b")[1][::-1]
    lengths = [2**i for i, el in enumerate(reversed_bin_string) if el == "1"]
    startpoint = 0
    big_list = []
    for l in lengths:
        big_list.append(ms(numbers[startpoint : startpoint + l]))
        startpoint += l

    return [" ".join([str(el) for el in reduce(merge, big_list)])]


def merge(seq1, seq2):
    int_seq1 = seq1
    int_seq2 = seq2
    left_idx, right_idx = 0, 0
    ordered_list = []
    while left_idx < len(int_seq1) and right_idx < len(int_seq2):
        if int_seq1[left_idx] <= int_seq2[right_idx]:
            ordered_list.append(int_seq1[left_idx])
            left_idx += 1
        else:
            ordered_list.append(int_seq2[right_idx])
            right_idx += 1
    if left_idx < len(int_seq1):
        ordered_list += int_seq1[left_idx:]
    else:
        ordered_list += int_seq2[right_idx:]

    return ordered_list


if __name__ == "__main__":

    data, filename = io.read_data("ms")
    # data = [
    #    "10",
    #    "20 19 35 -18 17 -20 20 1 4 41 13",
    # ]
    solution = merge_sort(data[1])
    # print(solution)
    io.write_data(solution=solution, filename=filename)
