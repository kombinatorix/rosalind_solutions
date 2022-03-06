"""
https://rosalind.info/problems/fibo/
"""
from src.utils.io import read_data, write_data


def calculate_fibonacci(n):
    fib = [0, 1]
    if n < 2:
        return [str(fib[n])]
    else:
        for k in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
    return [str(fib[-1])]


if __name__ == "__main__":

    data, filename = read_data("fibo")
    solution = calculate_fibonacci(int(data[0]))
    write_data(solution=solution, filename=filename)
