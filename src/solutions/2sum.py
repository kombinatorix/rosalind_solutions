"""
https://rosalind.info/problems/2sum/
"""
from src.utils.io import read_data, write_data


def get_indices(sequence):
    dict_number = dict()
    for idx, el in enumerate(sequence, start=1):
        if -el in dict_number.keys():
            return f"{dict_number[-el]} {idx}"
        else:
            dict_number[el] = idx
    return str(-1)


def compute_indices(sequences):
    results = []
    print(len(sequences))
    for seq in sequences:
        int_seq = list(map(lambda x: int(x), seq.split(" ")))
        results.append(get_indices(int_seq))
    return results  # [" ".join(results)]


if __name__ == "__main__":

    data, filename = read_data("2sum")
    solution = compute_indices(data[1:])
    write_data(solution=solution, filename=filename)
