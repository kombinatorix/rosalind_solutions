"""
https://rosalind.info/problems/ins/
"""
from src.utils.io import read_data, write_data


def insertion_sort(n, element_list):
    counter = 0
    A = list(map(lambda x: int(x), element_list.split(" ")))
    for i in range(1, n):
        k = i
        while (k > 0) and (A[k] < A[k - 1]):
            A[k - 1], A[k] = A[k], A[k - 1]
            k -= 1
            counter += 1

    return [str(counter)]


if __name__ == "__main__":

    data, filename = read_data("ins")
    solution = insertion_sort(int(data[0]), data[1])
    write_data(solution=solution, filename=filename)
