import urllib.request
import json
import config


def get_ability_scores() -> dict:

    ability_scores = {}
    abilities = []

    with urllib.request.urlopen(config.ABILITY_SCORES) as ability_response:
        data = json.loads(ability_response.read().decode())["results"]

        if data:
            for ability in data:
                abilities.append(ability["name"])

            ability_scores.setdefault(abilities[4], 0)
            ability_scores.setdefault(abilities[2], 0)
            ability_scores.setdefault(abilities[1], 0)
            ability_scores.setdefault(abilities[3], 0)
            ability_scores.setdefault(abilities[5], 0)
            ability_scores.setdefault(abilities[0], 0)

    return ability_scores


def get_race() -> list:

    races = []

    with urllib.request.urlopen(config.RACES) as races_response:
        data = json.loads(races_response.read().decode())["results"]

        if data:
            for race in data:
                races.append(race["name"])

    return races


def get_race_details(race: str, purpose="ability_bonuses") -> dict:

    ability_bonuses = {}
    traits = {}

    with urllib.request.urlopen(config.RACES + race) as race_details_response:
        data = json.loads(race_details_response.read().decode())

    if data:
        ability_bonuses = data["ability_bonuses"]
        traits = data["traits"]

    if purpose == "traits":
        return traits

    return ability_bonuses


def get_classes() -> list:

    classes = []

    with urllib.request.urlopen(config.CLASSES) as classes_response:
        data = json.loads(classes_response.read().decode())["results"]

        if data:
            for character_class in data:
                classes.append(character_class["name"])

    return classes


def get_class_details(character_class) -> dict:

    class_details = {}

    with urllib.request.urlopen(
        config.CLASSES + character_class
    ) as class_details_response:
        data = json.loads(class_details_response.read().decode())

        if data:
            class_details = data

    return class_details


def get_alignment() -> list:

    alignments = []

    with urllib.request.urlopen(config.ALIGNMENT) as alignment_response:
        data = json.loads(alignment_response.read().decode())["results"]

        if data:
            for alignment in data:
                alignments.append(alignment["name"])

    return alignments


def get_spells(character_class) -> list:

    spells = []

    with urllib.request.urlopen(
        config.CLASSES + character_class + "/spells"
    ) as spells_response:
        data = json.loads(spells_response.read().decode())["results"]

        if data:
            for spell in data:
                spells.append({"name": spell["name"], "level": spell["level"]})

    return spells
