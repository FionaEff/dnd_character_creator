def get_id(character_list: list[dict]) -> int:

    if not character_list:
        return 1

    id_list = [int(id) for entry in character_list for id in entry]

    if not id_list:
        return 1

    return max(id_list) + 1
