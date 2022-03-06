"""
https://rosalind.info/problems/subs/
"""
from src.utils.io import read_data, write_data
import re


def find_positions_of_seach_string(sequence, search_string):
    matches = re.finditer(r"(?=(" + search_string + "))", sequence)
    return [" ".join([str(match.start() + 1) for match in matches])]


if __name__ == "__main__":

    data, filename = read_data("subs")
    solution = find_positions_of_seach_string(sequence=data[0], search_string=data[1])
    write_data(solution=solution, filename=filename)
