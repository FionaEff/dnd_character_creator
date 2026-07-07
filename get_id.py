from read_characters import read_characters


def get_id() -> int:

    characters_list = read_characters()
    id_list = []
    id = 0

    for entry in characters_list:
        for id, details in entry.items():
            id_list.append(int(id))

    id = max(id_list) + 1

    return id
