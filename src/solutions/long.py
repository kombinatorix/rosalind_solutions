"""
https://rosalind.info/problems/long/
"""
from src.utils.io import read_fasta, write_data
from src.utils.genetic_string import GeneticString


def compute_shortest_superstring(genetic_strings):
    set_of_strings = {el for el in genetic_strings}
    tmp_longest = set_of_strings.pop()

    while len(set_of_strings) > 0:
        for gs in set_of_strings:
            if gs.max_overlap(tmp_longest) > len(gs.gen_string) / 2:
                tmp_longest = GeneticString(
                    "|#|"
                    + gs.gen_string[: -gs.max_overlap(tmp_longest)]
                    + tmp_longest.gen_string
                )
                set_of_strings.remove(gs)
                break
            if tmp_longest.max_overlap(gs) > len(gs.gen_string) / 2:
                tmp_longest = GeneticString(
                    "|#|"
                    + tmp_longest.gen_string[: -tmp_longest.max_overlap(gs)]
                    + gs.gen_string
                )
                set_of_strings.remove(gs)
                break
    return [tmp_longest.gen_string]


if __name__ == "__main__":

    data, filename = read_fasta("long")
    solution = compute_shortest_superstring(data)
    print(solution)
    write_data(solution=solution, filename=filename)
