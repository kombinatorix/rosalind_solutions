"""
https://rosalind.info/problems/prot/
"""
from src.utils import io
from src.utils import mappings

def translate_rna_to_prot(sequence):
    protein = [mappings.rna_codon_table[sequence[idx:idx+3]] for idx in range(0,len(sequence),3)]
    protein = "".join(protein).split("Stop")[0]
    return [f'{protein}']

if __name__ == "__main__":

    data, filename =  io.read_data("prot")
    #data = ["AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"]
    solution = translate_rna_to_prot(data[0])
    io.write_data(solution=solution, filename=filename)