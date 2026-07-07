from read_characters import read_characters
import json


def delete_character() -> None:

    character_list = read_characters()

    while True:
        id_input = str(input("\nPlease enter the ID of the character: "))
        if id_input.isdigit():
            break
        else:
            print("Please enter a valid ID!\n")

    for entry in character_list:
        for id, details in entry.items():
            if id == id_input:
                while True:
                    confirm = str(
                        input(
                            f"Do you want to delete \033[1m{details["name"]}\033[0m?\nConfirm with y/n: "
                        )
                    )
                    if confirm == "y":
                        character_list.remove(entry)
                        print(
                            f"Character \033[1m{details["name"]}\033[0m has been deleted!"
                        )

                        menu = str(input("\nPlease press Enter to continue ... "))
                        print("")

                        with open("./data/characters.json", "w") as file:
                            json.dump(character_list, file, indent=4)

                        return

                    elif confirm == "n":
                        print("Aborting ...\n")
                        break
                    else:
                        print("Please just use y and n to confirm or abort!")

    if id_input not in character_list:
        print("Character not found!")
        return
