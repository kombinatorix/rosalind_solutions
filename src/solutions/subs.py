"""
https://rosalind.info/problems/subs/
"""
from re import S
from src.utils import io
import re

def find_positions_of_seach_string(sequence, search_string):
    start = 0
    matches = re.finditer(r'(?=('+search_string+'))', sequence)
    return [" ".join([str(match.start()+1) for match in matches])]

if __name__ == "__main__":

    data, filename =  io.read_data("subs")
    #data = ["GATATATGCATATACTT", "ATAT"]
    solution = find_positions_of_seach_string(sequence=data[0], search_string=data[1])
    io.write_data(solution=solution, filename=filename)