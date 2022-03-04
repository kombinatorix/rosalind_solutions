from collections import Counter


class GeneticString(object):
    def __init__(self, input_string) -> None:
        first_line, *rest = input_string.split("|#|")
        name, *description = first_line.split(" ")
        self.name = name.replace(">", "").strip()
        self.description = " ".join(description)
        self.gen_string = "".join([el.strip() for el in rest])

    def calculate_percentage_of(self, list_of_symnols) -> int:
        counter = Counter(self.gen_string)
        occurances = sum([counter[el] for el in list_of_symnols])
        number_of_all_symbols = len(self.gen_string)
        return occurances / number_of_all_symbols * 100.0

    def find_pattern(self, pattern):
        positions = []
        for match in pattern.finditer(self.gen_string, overlapped=True):
            positions.append(str(match.start() + 1))
        return " ".join(positions)

    def overlap_k(self, other_gen_string, k: int):
        return self.gen_string[-k:] == other_gen_string.gen_string[:k]

    def max_overlap(self, other_gen_string):
        n = len(self.gen_string)
        for k in range(n, 0, -1):
            if self.overlap_k(other_gen_string, k):
                return k
        else:
            return 0


if __name__ == "__main__":
    genestic_string = GeneticString(
        ">MyName This is my description| TAGGTACAGACTCATGTAAGTAAGCGATGTGTGATTGGCGGGTTTAG | AGTC"
    )
    print(genestic_string.calculate_percentage_of(["G", "C"]))
