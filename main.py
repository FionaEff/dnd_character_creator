from create_character import create_character
from read_characters import print_characters, print_character_details
from delete_character import delete_character
from exception import NoDataError


def main():

    print("DnD 5e Character Creator\n")

    while True:
        print(f"""Select one of the following options using the number keys.
    1 - Show all characters
    2 - Show character details
    3 - Add random character
    4 - Delete character
    0 - Exit""")

        try:
            choice = int(input(""))

            match choice:
                case 1:
                    print_characters()
                case 2:
                    print_character_details()
                case 3:
                    try:
                        create_character()
                    except NoDataError as e:
                        print(e)
                case 4:
                    delete_character()
                case 0:
                    exit()
                case _:
                    print("Please just use numbers 1 - 4 and 0!\n")
        except ValueError:
            print("Please just use the number keys!/n")


main()
