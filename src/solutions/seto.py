"""
https://rosalind.info/problems/seto/
"""
from src.utils.io import read_data, write_data


def forming_sets(n, set_a, set_b):
    universe = {el for el in range(1, n + 1)}
    a_union_b = set_a.union(set_b)
    a_intersection_b = set_a.intersection(set_b)
    a_minus_b = set_a.difference(set_b)
    b_minus_a = set_b.difference(set_a)
    a_complement = universe.difference(set_a)
    b_complement = universe.difference(set_b)

    return [
        str(a_union_b),
        str(a_intersection_b),
        str(a_minus_b),
        str(b_minus_a),
        str(a_complement),
        str(b_complement),
    ]


if __name__ == "__main__":

    data, filename = read_data("seto")
    solution = forming_sets(int(data[0]), eval(data[1]), eval(data[2]))
    write_data(solution=solution, filename=filename)
