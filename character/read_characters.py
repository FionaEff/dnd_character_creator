import json
import os
from character.create_json import create_json


def read_characters() -> list:

    characters = []
    characters_file = "./data/characters.json"

    if not os.path.isfile(characters_file):
        create_json()

    with open("./data/characters.json", "r") as file:
        characters = json.load(file)

    return characters


def print_characters() -> None:

    character_list = read_characters()

    print("Characters:")
    print("-" * 11)

    for entry in character_list:
        for id, details in entry.items():
            print(
                f"\033[1mID:\033[0m {id:5}\033[1mName:\033[0m {details["name"]:25}\033[1mClass:\033[0m {details["class"]}"
            )

    menu = str(input("\nPlease press Enter to continue ... "))
    print("")


def print_character_details() -> None:

    character_list = read_characters()

    while True:
        id_input = str(input("Please enter the ID of the character: "))
        if id_input.isdigit():
            break
        else:
            print("Please enter a valid ID!\n")


    for entry in character_list:
        for id, details in entry.items():
            if id == id_input:
                print(f"\n{details["name"]}")
                print("-" * 20)
                for key, value in details.items():
                    if key != "ability scores" and key != "traits" and key != "spells":
                        print(f"\033[1m{key.capitalize()}:\033[0m {value}")

                    elif key == "ability scores":
                        print(f"\n\033[1m{key.title()}:\033[0m")
                        for ability, score in details["ability scores"].items():
                            print(f"{ability:>5}: {score}")

                    elif key == "traits":
                        print(f"\n\033[1m{key.capitalize()}:\033[0m {", ".join(value)}")

                    elif key == "spells":
                        print(f"\033[1m{key.capitalize()}:\033[0m {", ".join(value)}")

                menu = str(input("\nPlease press Enter to continue ... "))
                print("")

                return

    if id_input not in character_list:
        print("\nCharacter not found!\n")
        return

