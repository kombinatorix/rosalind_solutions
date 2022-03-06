"""
https://rosalind.info/problems/tree/
"""
from src.utils.io import read_data, write_data
from importlib import machinery
import networkx as nx


def compute_number_of_missing_edges(number_nodes, edges):
    g = nx.Graph()
    g.add_nodes_from([str(el) for el in range(1, number_nodes + 1)])
    for edge in edges:
        v, w = edge.split(" ")
        g.add_edge(v, w)
    return [str(len(list(nx.connected_components(g))) - 1)]


if __name__ == "__main__":

    data, filename = read_data("tree")
    solution = compute_number_of_missing_edges(int(data[0]), data[1:])
    write_data(solution=solution, filename=filename)
