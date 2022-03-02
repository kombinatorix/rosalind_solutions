"""
https://rosalind.info/problems/perm/
"""
from src.utils import io
from itertools import permutations

def compute_permutations(n):
    n_str = [str(el) for el in range(1, int(n)+1)]
    perms = [" ".join(perm) for perm in permutations(n_str)]
    return [str(len(perms))] + perms
    

if __name__ == "__main__":

    data, filename =  io.read_data("perm")
    solution = compute_permutations(data[0])
    io.write_data(solution=solution, filename=filename)