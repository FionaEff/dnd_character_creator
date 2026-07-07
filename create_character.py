from character import Character
from read_characters import read_characters
from get_id import get_id
import api
import random
import time
import json


def randomise_character(name) -> Character:

    race = random.choice(api.get_race())
    character_class = random.choice(api.get_classes())
    alignment = random.choice(api.get_alignment())
    hitpoints = 0
    level = 1

    random_character = Character(
        name, race, character_class, hitpoints, alignment, level
    )

    random_character.roll_ability_scores()
    random_character.apply_race_bonuses()
    random_character.starting_hitpoints()
    random_character.racial_traits()
    random_character.set_spells()

    return random_character


def create_character() -> None:

    character_list = read_characters()

    while True:
        name = str(input("Name your character: "))

        if len(name) < 3:
            print("Please enter a name!")
        else:
            break

    character = randomise_character(name)
    creation_time = time.strftime("%d.%m.%Y - %H:%M:%S")
    id = get_id()

    new_character = {
        id: {
            "name": name,
            "race": character.race,
            "class": character.character_class,
            "alignment": character.alignment,
            "hitpoints": character.hitpoints,
            "level": character.level,
            "ability scores": {
                "STR": character.ability_scores["STR"],
                "DEX": character.ability_scores["DEX"],
                "CON": character.ability_scores["CON"],
                "INT": character.ability_scores["INT"],
                "WIS": character.ability_scores["WIS"],
                "CHA": character.ability_scores["CHA"],
            },
            "traits": character.traits,
            "spells": character.spells,
            "created": creation_time,
        },
    }

    character_list.append(new_character)

    with open("./data/characters.json", "w") as file:

        json.dump(character_list, file, indent=4)

    print(f"New character {name} successfully added!")
