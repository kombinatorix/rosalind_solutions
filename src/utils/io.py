from os import listdir


def read_data(name):
    data_inputs = [el for el in listdir(path="data/input") if f"_{name}_" in el]
    for idx, input_filename in enumerate(data_inputs, start=1):
        print(f"{idx}. {input_filename}")
    filename = data_inputs[ int( input("Enter number of file: "))-1]

    with open(f"data/input/{filename}") as fp:
        data = fp.read().splitlines()
    
    return data, filename

def write_data(solution,filename):
    with open(f"data/output/{filename.replace('dataset','output')}", "w") as fp:
        fp.write("\n".join(solution))
