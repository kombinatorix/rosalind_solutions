"""
https://rosalind.info/problems/prtm/
"""
from src.utils import io, mappings

def calculate_protein_mass(sequence):
    return [f"{sum([mappings.monoisotopic_mass_table[el] for el in sequence]):.3f}"] 
    

if __name__ == "__main__":

    data, filename =  io.read_data("prtm")
    #data = ["SKADYEK"]
    solution = calculate_protein_mass(data[0])
    io.write_data(solution=solution, filename=filename)