"""
https://rosalind.info/problems/bins/
"""
from src.utils.io import read_data, write_data


def binary_search(sorted_list_of_ints, searched_value):
    left = 0
    right = len(sorted_list_of_ints) - 1
    middle = 0

    while left <= right:

        middle = (right + left) // 2

        if sorted_list_of_ints[middle] < searched_value:
            left = middle + 1

        elif sorted_list_of_ints[middle] > searched_value:
            right = middle - 1

        else:
            return middle + 1  # for index beginning with 1

    return -1


def values_present(search_for, search_in):
    search_for = list(map(lambda x: int(x), search_for.split(" ")))
    search_in = sorted(list(map(lambda x: int(x), search_in.split(" "))))

    return [" ".join([str(binary_search(search_in, el)) for el in search_for])]


if __name__ == "__main__":

    data, filename = read_data("bins")
    solution = values_present(data[3], data[2])
    write_data(solution=solution, filename=filename)
