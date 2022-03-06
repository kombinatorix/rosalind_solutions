"""
https://rosalind.info/problems/fib/
"""
from src.utils.io import read_data, write_data


def general_fibonacci(input_string):
    n, k = map(lambda x: int(x), input_string.split(" "))
    generations = [1, 1]
    if n > 2:
        for _ in range(3, n + 1):
            generations.append(generations[-1] + k * generations[-2])
    return [str(generations[n - 1])]


if __name__ == "__main__":

    data, filename = read_data("fibd")
    solution = general_fibonacci(data[0])
    write_data(solution=solution, filename=filename)
