from character.read_characters import read_characters
import json


def delete_character() -> None:

    character_list = read_characters()
    id_found = False

    while True:
        id_input = str(input("\nPlease enter the ID of the character: "))
        if id_input.isdigit():
            break
        else:
            print("Please enter a valid ID!\n")

    for entry in character_list:
        if id_input in entry:
            id_found = True
            details = entry[id_input]

            while True:
                confirm = str(
                    input(
                        f"Do you want to delete \033[1m{details['name']}\033[0m?\nConfirm with y/n: "
                    ).lower()
                )
                if confirm == "y":
                    character_list.remove(entry)

                    with open("./data/characters.json", "w") as file:
                        json.dump(character_list, file, indent=4)

                    print(
                        f"Character \033[1m{details['name']}\033[0m has been deleted!"
                    )

                    menu = str(input("\nPlease press Enter to continue ... "))
                    print("")

                    return

                elif confirm == "n":
                    print("Aborting ...\n")
                    break
                else:
                    print("Please just use y and n to confirm or abort!")

    if not id_found:
        print("Character not found!")
        return
