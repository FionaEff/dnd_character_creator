import random
from api.api import get_ability_scores, get_class_details, get_race_details, get_spells


class Character:

    def __init__(
        self, name, race, character_class, hitpoints, alignment="neutral", level=1
    ) -> None:
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hitpoints = hitpoints
        self.alignment = alignment
        self.traits = []
        self.spells = []
        self.ability_scores = {}

    def roll_ability_scores(self) -> None:

        scores = []
        dice_rolls = []
        self.ability_scores = get_ability_scores()

        while len(scores) < 6:

            for _ in range(4):
                roll = random.randint(1, 6)
                dice_rolls.append(roll)

            min_roll = min(dice_rolls)
            dice_rolls.remove(min_roll)
            ability_score = sum(dice_rolls)
            scores.append(ability_score)
            dice_rolls.clear()

        self.ability_scores.update(
            {
                "STR": scores[0],
                "DEX": scores[1],
                "CON": scores[2],
                "INT": scores[3],
                "WIS": scores[4],
                "CHA": scores[5],
            }
        )

    def starting_hitpoints(self) -> None:

        hit_die = get_class_details(self.character_class.lower())["hit_die"]

        self.hitpoints = hit_die + ((self.ability_scores["CON"] - 10) // 2)

    def apply_race_bonuses(self):

        bonuses = get_race_details(self.race.lower(), "ability_bonuses")

        for bonus in bonuses:
            ability = bonus["ability_score"]["name"]
            score = bonus["bonus"] + self.ability_scores[ability]
            self.ability_scores.update({ability: score})

    def racial_traits(self) -> None:

        traits = get_race_details(self.race.lower(), "traits")

        for trait in traits:
            self.traits.append(trait["name"])

    def set_spells(self) -> None:

        class_details = get_class_details(self.character_class.lower())

        if "spellcasting" in class_details:
            spell_list = get_spells(self.character_class.lower())

            for spell in spell_list:
                if spell["level"] == 0 or spell["level"] == 1:
                    self.spells.append(spell["name"])
                    if len(self.spells) == 3:
                        break
