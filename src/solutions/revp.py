"""
https://rosalind.info/problems/revp/
"""
from src.utils.io import read_fasta, write_data
from src.utils.mappings import dna_complements


def is_reverse_palindrome(string):
    return string == "".join([dna_complements[el] for el in string[::-1]])


def locating_restriction_sites(genetic_string):
    result = []
    for length in range(4, 12 + 1):
        for pos, _ in enumerate(genetic_string.gen_string):
            sub_string = genetic_string.gen_string[pos : pos + length]
            if len(sub_string) == length and is_reverse_palindrome(sub_string):
                result.append(f"{pos+1} {length}")
    return result


if __name__ == "__main__":

    data, filename = read_fasta("revp")
    solution = locating_restriction_sites(data[0])
    write_data(solution=solution, filename=filename)
