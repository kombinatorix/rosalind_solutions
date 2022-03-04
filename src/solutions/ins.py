"""
https://rosalind.info/problems/ins/
"""
from src.utils import io


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

    data, filename = io.read_data("ins")
    # data = [
    #    "6",
    #    "6 10 4 5 1 2",
    # ]
    solution = insertion_sort(int(data[0]), data[1])
    # print(solution)
    io.write_data(solution=solution, filename=filename)
