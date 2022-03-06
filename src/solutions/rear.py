"""
https://rosalind.info/problems/rear/
"""
from src.utils.io import read_data, write_data
from multiprocessing import Pool


def calculate_slices_from_2_to_n(n):
    list_of_slices = []
    for idx in range(0, n):
        for width in range(2, n + 1):
            if idx + width <= n:
                list_of_slices.append(slice(idx, idx + width))
    return list_of_slices


def reverse_tuple(tuple_1, slice_1):
    before = tuple_1[0 : slice_1.start]
    middle = tuple_1[slice_1][::-1]
    end = tuple_1[slice_1.stop :]
    return tuple(el for el in before + middle + end)


def calculate_reversal_distance(sequences):
    seq1, seq2 = sequences
    n = len(seq1)
    sequence1 = tuple(int(el) for el in seq1.split(" "))
    sequence2 = tuple(int(el) for el in seq2.split(" "))
    list_of_slices = calculate_slices_from_2_to_n(n)
    counter = 0
    next_to_expand_1 = set()
    next_to_expand_1.add(sequence1)
    already_expanded_1 = set()
    next_to_expand_2 = set()
    next_to_expand_2.add(sequence2)
    already_expanded_2 = set()
    while True:
        if sequence2 in next_to_expand_1:
            return str(counter)
        elif len(next_to_expand_1.intersection(already_expanded_2)) > 1:
            return str(counter * 2 - 1)
        elif len(next_to_expand_2.intersection(already_expanded_1)) > 1:
            return str(counter * 2 - 1)
        elif len(next_to_expand_1.intersection(next_to_expand_2)) > 1:
            return str(counter * 2)
        else:
            already_expanded_1.update(next_to_expand_1)
            potential_expands_1 = set()
            for sequence in next_to_expand_1:
                potential_expands_1.update(
                    {reverse_tuple(sequence, s) for s in list_of_slices}
                )
            next_to_expand_1 = potential_expands_1.difference(already_expanded_1)
            already_expanded_2.update(next_to_expand_2)
            potential_expands_2 = set()
            for sequence in next_to_expand_2:
                potential_expands_2.update(
                    {reverse_tuple(sequence, s) for s in list_of_slices}
                )
            next_to_expand_2 = potential_expands_2.difference(already_expanded_1)
            counter += 1


def calculate_list_of_reversal_distances(data):
    list_of_inputs = [[data[i], data[i + 1]] for i in range(0, len(data), 3)]
    p = Pool(5)
    with p:
        return [" ".join(p.map(calculate_reversal_distance, list_of_inputs))]


if __name__ == "__main__":

    data, filename = read_data("rear")
    solution = calculate_list_of_reversal_distances(data)
    write_data(solution=solution, filename=filename)
