"""
https://rosalind.info/problems/fibo/
"""
from src.utils import io


def calculate_fibonacci(n):
    fib = [0, 1]
    if n < 2:
        return [str(fib[n])]
    else:
        for k in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
    return [str(fib[-1])]


if __name__ == "__main__":

    data, filename = io.read_data("fibo")
    # data = ["6"]
    solution = calculate_fibonacci(int(data[0]))
    # print(solution)
    io.write_data(solution=solution, filename=filename)
