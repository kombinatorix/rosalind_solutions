"""
https://rosalind.info/problems/rear/
"""
from src.utils import io
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

    data, filename = io.read_data("rear")
    # data = [
    #    "1 2 3 4 5 6 7 8 9 10",
    #    "3 1 5 2 7 4 9 6 10 8",
    #    "",
    #    "3 10 8 2 5 4 7 1 6 9",
    #    "5 2 3 1 7 4 10 8 6 9",
    #    "",
    #    "8 6 7 9 4 1 3 10 2 5",
    #    "8 2 7 6 9 1 5 3 10 4",
    #    "",
    #    "3 9 10 4 1 8 6 7 5 2",
    #    "2 9 8 5 1 7 3 4 6 10",
    #    "",
    #    "1 2 3 4 5 6 7 8 9 10",
    #    "1 2 3 4 5 6 7 8 9 10",
    # ]
    solution = calculate_list_of_reversal_distances(data)
    io.write_data(solution=solution, filename=filename)
