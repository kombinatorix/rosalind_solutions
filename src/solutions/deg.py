"""
https://rosalind.info/problems/deg/
"""
from src.utils.io import read_data, write_data


def empty_list():
    return []


def degree_array(info, edge_sequence):
    n = int(info.split(" ")[0])
    neigbhoorhood = {i: [] for i in range(1, n + 1)}
    for edge in edge_sequence:
        v, w = map(lambda x: int(x), edge.split(" "))
        neigbhoorhood[v].append(w)
        neigbhoorhood[w].append(v)

    return [
        " ".join([str(len(neigbhoorhood[idx])) for idx in sorted(neigbhoorhood.keys())])
    ]


if __name__ == "__main__":

    data, filename = read_data("deg")
    solution = degree_array(data[0], data[1:])
    write_data(solution=solution, filename=filename)
