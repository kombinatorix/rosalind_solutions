"""
https://rosalind.info/problems/deg/
"""
from src.utils import io


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

    data, filename = io.read_data("deg")
    # data = [
    #    "6 7",
    #    "1 2",
    #    "2 3",
    #    "6 3",
    #    "5 6",
    #    "2 5",
    #    "2 4",
    #    "4 1",
    # ]
    solution = degree_array(data[0], data[1:])
    # print(solution)
    io.write_data(solution=solution, filename=filename)
