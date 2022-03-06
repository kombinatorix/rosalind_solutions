"""
https://rosalind.info/problems/rear/
"""
from src.utils.io import read_data, write_data
from multiprocessing import Pool
from importlib import machinery
import networkx as nx


def empty_list():
    return []


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


def get_slices_from_shortest_path(graph, start_node, end_node):
    shortest_path = nx.shortest_path(graph, source=start_node, target=end_node)
    print(shortest_path)
    slice_list = []
    path_graph = nx.path_graph(shortest_path)
    for edge in path_graph.edges():
        s = graph.edges[edge[0], edge[1]]["slice"]
        slice_list.append(f"{s[0]+1} {s[1]}")
    return [str(len(shortest_path) - 1)] + slice_list


def calculate_list_of_reversal_distances(sequences):
    seq1, seq2 = sequences
    sequence1 = tuple(int(el) for el in seq1.split(" "))
    sequence2 = tuple(int(el) for el in seq2.split(" "))
    n = len(sequence1)
    list_of_slices = calculate_slices_from_2_to_n(n)
    counter = 0
    next_to_expand_1 = set()
    next_to_expand_1.add(sequence1)
    already_expanded_1 = set()
    next_to_expand_2 = set()
    next_to_expand_2.add(sequence2)
    already_expanded_2 = set()
    g = nx.Graph()
    while True:
        print(counter)
        if sequence2 == sequence1:
            return [str(counter)]
        elif len(next_to_expand_1.intersection(already_expanded_2)) > 1:
            return get_slices_from_shortest_path(
                graph=g, start_node=sequence1, end_node=sequence2
            )
        elif len(next_to_expand_2.intersection(already_expanded_1)) > 1:
            return get_slices_from_shortest_path(
                graph=g, start_node=sequence1, end_node=sequence2
            )
        elif len(next_to_expand_1.intersection(next_to_expand_2)) > 1:
            return get_slices_from_shortest_path(
                graph=g, start_node=sequence1, end_node=sequence2
            )
        else:
            already_expanded_1.update(next_to_expand_1)
            potential_expands_1 = set()
            for sequence in next_to_expand_1:
                tmp_dict = {
                    reverse_tuple(sequence, s): (s.start, s.stop)
                    for s in list_of_slices
                }
                potential_expands_1.update(set(tmp_dict.keys()))
                for node, slice_ in tmp_dict.items():
                    g.add_edge(sequence, node, slice=slice_)
            next_to_expand_1 = potential_expands_1.difference(already_expanded_1)
            already_expanded_2.update(next_to_expand_2)
            potential_expands_2 = set()
            for sequence in next_to_expand_2:
                tmp_dict = {
                    reverse_tuple(sequence, s): (s.start, s.stop)
                    for s in list_of_slices
                }
                for node, slice_ in tmp_dict.items():
                    g.add_edge(sequence, node, slice=slice_)
                potential_expands_2.update(set(tmp_dict.keys()))
            next_to_expand_2 = potential_expands_2.difference(already_expanded_1)
            counter += 1
            # print(dict_history_1)


if __name__ == "__main__":

    data, filename = read_data("sort")
    solution = calculate_list_of_reversal_distances(data)
    write_data(solution=solution, filename=filename)
