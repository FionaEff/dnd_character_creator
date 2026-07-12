import urllib.request
import urllib.error
import json
import api.config as config
from exception.exception import NoDataError


def get_ability_scores() -> dict:

    ability_scores = {}
    abilities = []

    try:
        with urllib.request.urlopen(config.ABILITY_SCORES) as ability_response:
            data = json.loads(ability_response.read().decode())["results"]

            for ability in data:
                abilities.append(ability["name"])

            ability_scores.setdefault(abilities[4], 0)
            ability_scores.setdefault(abilities[2], 0)
            ability_scores.setdefault(abilities[1], 0)
            ability_scores.setdefault(abilities[3], 0)
            ability_scores.setdefault(abilities[5], 0)
            ability_scores.setdefault(abilities[0], 0)

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return ability_scores


def get_race() -> list:

    races = []

    try:
        with urllib.request.urlopen(config.RACES) as races_response:
            data = json.loads(races_response.read().decode())["results"]

            for race in data:
                races.append(race["name"])

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return races


def get_race_details(race: str, purpose="ability_bonuses") -> dict:

    ability_bonuses = {}
    traits = {}

    try:
        with urllib.request.urlopen(config.RACES + race) as race_details_response:
            data = json.loads(race_details_response.read().decode())

            ability_bonuses = data["ability_bonuses"]
            traits = data["traits"]

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    if purpose == "traits":
        return traits

    return ability_bonuses


def get_classes() -> list:

    classes = []

    try:
        with urllib.request.urlopen(config.CLASSES) as classes_response:
            data = json.loads(classes_response.read().decode())["results"]

            for character_class in data:
                classes.append(character_class["name"])

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return classes


def get_class_details(character_class) -> dict:

    class_details = {}

    try:
        with urllib.request.urlopen(
            config.CLASSES + character_class
        ) as class_details_response:
            data = json.loads(class_details_response.read().decode())

            class_details = data

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return class_details


def get_alignment() -> list:

    alignments = []

    try:
        with urllib.request.urlopen(config.ALIGNMENT) as alignment_response:
            data = json.loads(alignment_response.read().decode())["results"]

            for alignment in data:
                alignments.append(alignment["name"])

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return alignments


def get_spells(character_class) -> list:

    spells = []

    try:
        with urllib.request.urlopen(
            config.CLASSES + character_class + "/spells"
        ) as spells_response:
            data = json.loads(spells_response.read().decode())["results"]

            for spell in data:
                spells.append({"name": spell["name"], "level": spell["level"]})

    except urllib.error.HTTPError as err:
        print(f"An error happened! Error Code {err.code}: Reason: {err.reason}")
        raise NoDataError

    except urllib.error.URLError as err:
        print(f"An error happened! Reason: {err.reason}")
        raise NoDataError

    return spells
