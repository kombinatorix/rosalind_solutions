from os import listdir
from src.utils.genetic_string import GeneticString


def read_data(name):
    data_inputs = [el for el in listdir(path="data/input") if f"_{name}" in el]
    for idx, input_filename in enumerate(data_inputs, start=1):
        print(f"{idx}. {input_filename}")
    filename = data_inputs[int(input("Enter number of file: ")) - 1]

    with open(f"data/input/{filename}") as fp:
        data = fp.read().splitlines()

    return data, filename


def data_to_genetic_string(data):
    concated_lines = " ".join(
        [f"+{line}" if ">" in line else f"|#| {line}" for line in data]
    )
    pre_genetic_strings = concated_lines.split("+")[1:]
    genetic_strings = [GeneticString(el) for el in pre_genetic_strings]
    return genetic_strings


def read_fasta(name):
    data, filename = read_data(name)
    genetic_strings = data_to_genetic_string(data)
    return genetic_strings, filename


def write_data(solution, filename):
    with open(f"data/output/{filename.replace('dataset','output')}", "w") as fp:
        fp.write("\n".join(solution))
