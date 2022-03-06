"""
https://rosalind.info/problems/ddeg/
"""
from src.utils.io import read_data, write_data


def sum_of_neighboordegrees(neighborhood, list_of_neighbors):
    if len(list_of_neighbors) == 0:
        return 0
    else:
        return sum([len(neighborhood[el]) for el in list_of_neighbors])


def double_degree_array(info, edge_sequence):
    n = int(info.split(" ")[0])
    neigbhoorhood = {i: [] for i in range(1, n + 1)}
    for edge in edge_sequence:
        v, w = map(lambda x: int(x), edge.split(" "))
        neigbhoorhood[v].append(w)
        neigbhoorhood[w].append(v)

    return [
        " ".join(
            [
                str(sum_of_neighboordegrees(neigbhoorhood, neigbhoorhood[idx]))
                for idx in sorted(neigbhoorhood.keys())
            ]
        )
    ]


if __name__ == "__main__":

    data, filename = read_data("ddeg")
    solution = double_degree_array(data[0], data[1:])
    write_data(solution=solution, filename=filename)
