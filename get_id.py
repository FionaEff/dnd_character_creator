from read_characters import read_characters


def get_id() -> int:

    characters_list = read_characters()
    id = 0

    id_list = [int(id) for entry in characters_list for id in entry]

    id = max(id_list) + 1

    return id
