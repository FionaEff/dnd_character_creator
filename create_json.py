import json

def create_json():

    character_list = []

    with open("./data/characters.json", "w") as file:
        json.dump(character_list, file)