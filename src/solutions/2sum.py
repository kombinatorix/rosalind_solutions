"""
https://rosalind.info/problems/2sum/
"""
from src.utils import io


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

    data, filename = io.read_data("2sum")
    # data = [
    #    "4 5",
    #    "2 -3 4 10 5",
    #    "8 2 4 -2 -8",
    #    "-5 2 3 2 -4",
    #    "5 4 -5 6 8",
    # ]
    solution = compute_indices(data[1:])
    # print(solution)
    io.write_data(solution=solution, filename=filename)
