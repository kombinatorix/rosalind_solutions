"""
https://rosalind.info/problems/mprt/
"""

from src.utils.io import read_data, write_data
from src.utils.genetic_string import GeneticString
import requests
import regex


def request_fasta(id):
    r = requests.get(f"https://www.uniprot.org/uniprot/{id}.fasta")
    return r.text.replace("\n", " |#| ")


def finding_protein_motif(list_of_access_ids):
    genetic_strings = [GeneticString(request_fasta(id)) for id in list_of_access_ids]
    pattern = regex.compile("N[^P][S|T][^P]")
    return_list = []
    for gen_string, id in zip(genetic_strings, list_of_access_ids):
        if gen_string.find_pattern(pattern) != "":
            return_list.append(id)
            return_list.append(gen_string.find_pattern(pattern))
    return return_list


if __name__ == "__main__":

    data, filename = read_data("mprt")
    solution = finding_protein_motif(data)
    write_data(solution=solution, filename=filename)
