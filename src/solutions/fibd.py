"""
https://rosalind.info/problems/fibd/
"""
from src.utils.io import read_data, write_data


def general_fibonacci(input_string):
    n, m = map(lambda x: int(x), input_string.split(" "))
    f = [1, 1]
    b = [1, 0]
    if n > 2:
        for gen in range(3, n + 1):
            b.append(f[-1] - b[-1])
            if gen - m - 1 >= 0:
                b1 = b[gen - m - 1]
            else:
                b1 = 0
            if gen - m - 1 - 1 >= 0:
                b2 = b[gen - m - 1 - 1]
            else:
                b2 = 0
            f.append(f[-1] + f[-2] - b1 - b2)
    return [str(f[n - 1])]


if __name__ == "__main__":

    data, filename = read_data("fibd")
    solution = general_fibonacci(data[0])
    write_data(solution=solution, filename=filename)
