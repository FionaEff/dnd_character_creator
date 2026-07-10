from character.read_characters import read_characters


def get_ids() -> list:

    character_list = read_characters()
    id_list = []

    if character_list:
        id_list = [int(id) for entry in character_list for id in entry]

    else:
        id_list.append(0)

    return id_list


def highest_id() -> int:

    id_list = get_ids()

    return max(id_list)


def new_id() -> int:

    max_id = highest_id()

    return max_id + 1
