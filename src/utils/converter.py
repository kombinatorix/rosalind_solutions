def string_to_ints(string):
    return map(lambda x: int(x), string.split(" "))


def string_to_list_ints(string):
    return list(string_to_ints(string))


def list_ints_to_string(list_of_ints):
    return " ".join([str(el) for el in list_of_ints])
