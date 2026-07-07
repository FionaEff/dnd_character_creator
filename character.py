import random
from api import get_ability_scores, get_class_details, get_race_details, get_spells


class Character:

    ability_scores = get_ability_scores()
    traits = []
    spells = []

    def __init__(
        self, name, race, character_class, hitpoints, alignment="neutral", level=1
    ):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hitpoints = hitpoints
        self.alignment = alignment

    def roll_ability_scores(self):

        scores = []
        dice_rolls = []

        while len(scores) < 6:

            for _ in range(4):
                roll = random.randint(1, 6)
                dice_rolls.append(roll)

            min_roll = min(dice_rolls)
            dice_rolls.remove(min_roll)
            ability_score = sum(dice_rolls)
            scores.append(ability_score)
            dice_rolls.clear()

        Character.ability_scores.update(
            {
                "STR": scores[0],
                "DEX": scores[1],
                "CON": scores[2],
                "INT": scores[3],
                "WIS": scores[4],
                "CHA": scores[5],
            }
        )

    def starting_hitpoints(self):

        hit_die = get_class_details(self.character_class.lower())["hit_die"]
        self.hitpoints = hit_die + ((Character.ability_scores["CON"] - 10) // 2)

    def apply_race_bonuses(self):

        bonuses = get_race_details(self.race.lower(), "ability_bonuses")

        for bonus in bonuses:
            ability = bonus["ability_score"]["name"]
            score = bonus["bonus"] + Character.ability_scores[ability]
            Character.ability_scores.update({ability: score})

    def racial_traits(self):

        traits = get_race_details(self.race.lower(), "traits")

        for trait in traits:
            Character.traits.append(trait["name"])

    def set_spells(self):

        class_details = get_class_details(self.character_class.lower())
        spell_list = get_spells(self.character_class.lower())

        if "spellcasting" in class_details:

            for spell in spell_list:
                if spell["level"] == 0 or spell["level"] == 1:
                    Character.spells.append(spell["name"])
                    if len(Character.spells) == 3:
                        break

    def increase_level(self):

        self.level += 1

    def change_hitpoints(self, healing=0, damage=0):

        if healing > 0:
            self.hitpoints += healing
        else:
            self.hitpoints -= damage
