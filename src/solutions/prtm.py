"""
https://rosalind.info/problems/prtm/
"""
from src.utils.io import read_data, write_data
from src.utils.mappings import monoisotopic_mass_table


def calculate_protein_mass(sequence):
    return [f"{sum([monoisotopic_mass_table[el] for el in sequence]):.3f}"]


if __name__ == "__main__":

    data, filename = read_data("prtm")
    solution = calculate_protein_mass(data[0])
    write_data(solution=solution, filename=filename)
