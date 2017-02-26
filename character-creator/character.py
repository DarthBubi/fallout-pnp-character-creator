import calc_skills
import math

__author__ = "Johannes Hackbarth"


class FalloutCharacter(object):

    def __init__(self):
        # characteristics
        self.name = "Your Name"
        self.age = 0
        self.sex = ""
        self.eyes = "Colour"
        self.hair = "Colour"
        self.height = 1.0
        self.weight = 50.0
        self.appearance = "Describe your appearance"
        self.level = 1
        self.karma = 0
        self.experience = 0
        self.wounds = 0
        self.hit_points = 0

        # attributes
        self.strength = (0, {})
        self.perception = (0, {})
        self.endurance = (0, {})
        self.charisma = (0, {})
        self.intelligence = (0, {})
        self.agility = (0, {})
        self.luck = (0, {})

        # skills
        self.small_guns = 0
        self.big_guns = 0
        self.energy_weapons = 0
        self.unarmed = 0
        self.melee_weapons = 0
        self.throwing = 0
        self.explosives = 0
        self.doctor = 0
        self.sneak = 0
        self.lockpick = 0
        self.traps = 0
        self.science = 0
        self.repair = 0
        self.pilot = 0
        self.speech = 0
        self.barter = 0
        self.gambling = 0
        self.survival = 0

        self.tagged_skills = []
        self.traits = {}
        self.perks = []

    def total_value(self, attr):
        return attr[0] + sum(attr[1].values())

    def calculate_base_skills(self, bonus=0):
        self.small_guns = calc_skills.calculate_small_guns(self.total_value(self.agility)) + bonus
        self.big_guns = calc_skills.calculate_big_guns(self.total_value(self.strength),
                                                       self.total_value(self.perception),
                                                       self.total_value(self.endurance)) + bonus
        self.energy_weapons = calc_skills.calculate_energy_weapons(self.total_value(self.perception),
                                                                   self.total_value(self.intelligence)) + bonus
        self.unarmed = calc_skills.calculate_unarmed(self.total_value(self.agility),
                                                     self.total_value(self.strength)) + bonus
        self.melee_weapons = calc_skills.calculate_unarmed(self.total_value(self.agility),
                                                           self.total_value(self.strength)) + bonus
        self.throwing = calc_skills.calculate_throwing(self.total_value(self.agility)) + bonus
        self.explosives = calc_skills.calculate_explosives(self.total_value(self.perception),
                                                           self.total_value(self.luck)) + bonus
        self.doctor = calc_skills.calculate_doctor(self.total_value(self.perception),
                                                   self.total_value(self.endurance)) + bonus
        self.sneak = calc_skills.calculate_sneak(self.total_value(self.agility)) + bonus
        self.lockpick = calc_skills.calculate_lockpick(self.total_value(self.perception),
                                                       self.total_value(self.agility)) + bonus
        self.traps = calc_skills.caclulate_traps(self.total_value(self.perception),
                                                 self.total_value(self.agility)) + bonus
        self.science = calc_skills.calculate_science(self.total_value(self.intelligence)) + bonus
        self.repair = calc_skills.calculate_repair(self.total_value(self.intelligence)) + bonus
        self.pilot = calc_skills.calculate_pilot(self.total_value(self.agility),
                                                 self.total_value(self.perception)) + bonus
        self.speech = calc_skills.calculate_speech(self.total_value(self.charisma)) + bonus
        self.barter = calc_skills.calculate_barter(self.total_value(self.charisma)) + bonus
        self.gambling = calc_skills.calculate_gambling(self.total_value(self.perception),
                                                       self.total_value(self.luck)) + bonus
        self.survival = calc_skills.calculate_survival(self.total_value(self.endurance),
                                                       self.total_value(self.intelligence)) + bonus

    def calculate_base_hit_points(self):
        return 15 + self.total_value(self.strength) + 2 * self.total_value(self.endurance)

    def calculate_base_action_points(self):
        return int(self.total_value(self.agility) / 2 + 5)

    def calculate_carry_weight(self):
        return 15 * self.total_value(self.strength) if self.has_trait("Small Frame") else 25 + 25 * self.total_value(
            self.strength)

    def calculate_melee_damage(self):
        melee_damage = 1
        if self.total_value(self.strength) > 5:
            melee_damage = self.total_value(self.strength) - 5

        if self.has_trait("Heavy Handed"):
            melee_damage += 4
        elif self.has_trait("Domesticated"):
            melee_damage -= 2

        return melee_damage

    def add_trait(self, trait):
        if len(self.traits) < 2 and trait not in self.traits:
            self.traits.update({trait.name: trait})

    def has_trait(self, trait_name):
        return any(trait.name == trait_name for trait in self.traits)

    def remove_trait(self, trait):
        del self.traits[trait.name]

    def calculate_poison_resistance(self):
        return 5 * self.total_value(self.endurance)

    def calculate_radiation_resistance(self):
        return 2 * self.total_value(self.endurance)

    def calculate_gas_resistance(self):
        return 0, 0

    def calculate_electricity_resistance(self):
        return 0

    def calculate_damage_resistance(self):
        return (self.total_value(self.agility) + self.total_value(self.perception)) * 2 if self.has_trait(
            "Tight Nuts") else self.total_value(self.agility) + self.total_value(self.perception)

    def calculate_healing_rate(self):
        return int(self.total_value(self.endurance) / 3) + 2 if self.has_trait("Fast Metabolism") else int(
            self.total_value(self.endurance) / 3)

    def calculate_armor_class(self):
        return self.total_value(self.agility) + 10 if self.has_trait("Vat Skin") else self.total_value(self.agility)

    def taggable_skills(self):
        return 4 if self.has_trait("Beta Software") else 3


class Trait(object):
    def __init__(self, name, description, races, attr_mod=0, attr_name="", skill_mod=0, misc_mod=0):
        self.name = name
        self.description = description
        self.races = races
        self.attribute_mod = (attr_mod, attr_name)
        self.skill_mod = skill_mod
        self.misc_mod = misc_mod

    def __str__(self, *args, **kwargs):
        return self.name


class Perk(Trait):
    def __init__(self, name, description, races, level=0, attr_mod=0, skill_mod=0, misc_mod=0):
        super(Perk, self).__init__(name, description, races, attr_mod, skill_mod, misc_mod)
        self.level = level


class HumanCharacter(FalloutCharacter):
    MIN_STRENGTH = 1
    MAX_STRENGTH = 10
    MIN_PERCEPTION = 1
    MAX_PERCEPTION = 10
    MIN_ENDURANCE = 1
    MAX_ENDURANCE = 10
    MIN_CHARISMA = 1
    MAX_CHARISMA = 10
    MIN_INTELLIGENCE = 1
    MAX_INTELLIGENCE = 10
    MIN_AGILITY = 1
    MAX_AGILITY = 10
    MIN_LUCK = 1
    MAX_LUCK = 10

    def __init__(self):
        super(HumanCharacter, self).__init__()
        FalloutCharacter.MIN_STRENGTH = 1
        FalloutCharacter.MAX_STRENGTH = 10
        self.strength = 5, {}
        self.perception = 5, {}
        self.endurance = 5, {}
        self.charisma = 5, {}
        self.intelligence = 5, {}
        self.agility = 5, {}
        self.luck = 5, {}

    def calculate_electricity_resistance(self):
        return 10

    def __str__(self):
        return "Human"


class GhoulCharacter(FalloutCharacter):
    MIN_STRENGTH = 1
    MAX_STRENGTH = 2
    MIN_PERCEPTION = 4
    MAX_PERCEPTION = 13
    MIN_ENDURANCE = 1
    MAX_ENDURANCE = 10
    MIN_CHARISMA = 1
    MAX_CHARISMA = 10
    MIN_INTELLIGENCE = 2
    MAX_INTELLIGENCE = 10
    MIN_AGILITY = 1
    MAX_AGILITY = 6
    MIN_LUCK = 5
    MAX_LUCK = 12

    def __init__(self):
        super(GhoulCharacter, self).__init__()

        self.strength = 3, {}
        self.perception = 8, {}
        self.endurance = 5, {}
        self.charisma = 4, {}
        self.intelligence = 6, {}
        self.agility = 4, {}
        self.luck = 7, {}

    def calculate_electricity_resistance(self):
        return 10

    def calculate_poison_resistance(self):
        return super().calculate_poison_resistance() + 10

    def calculate_radiation_resistance(self):
        return super().calculate_radiation_resistance() + 40

    def __str__(self):
        return "Ghoul"


class SuperMutantCharacter(FalloutCharacter):
    MIN_STRENGTH = 5
    MAX_STRENGTH = 13
    MIN_PERCEPTION = 1
    MAX_PERCEPTION = 10
    MIN_ENDURANCE = 4
    MAX_ENDURANCE = 12
    MIN_CHARISMA = 1
    MAX_CHARISMA = 7
    MIN_INTELLIGENCE = 1
    MAX_INTELLIGENCE = 11
    MIN_AGILITY = 1
    MAX_AGILITY = 8
    MIN_LUCK = 1
    MAX_LUCK = 10

    def __init__(self):
        super(SuperMutantCharacter, self).__init__()

        self.strength = 8, {}
        self.perception = 6, {}
        self.endurance = 6, {}
        self.charisma = 5, {}
        self.intelligence = 5, {}
        self.agility = 4, {}
        self.luck = 5, {}

    def calculate_electricity_resistance(self):
        return 10

    def calculate_gas_resistance(self):
        return 0, 35

    def calculate_poison_resistance(self):
        return super().calculate_poison_resistance() + 20

    def calculate_radiation_resistance(self):
        return super().calculate_radiation_resistance() + 20

    def __str__(self):
        return "Super Mutant"


class HalfMutantCharacter(FalloutCharacter):
    MIN_STRENGTH = 3
    MAX_STRENGTH = 12
    MIN_PERCEPTION = 1
    MAX_PERCEPTION = 10
    MIN_ENDURANCE = 2
    MAX_ENDURANCE = 11
    MIN_CHARISMA = 1
    MAX_CHARISMA = 10
    MIN_INTELLIGENCE = 1
    MAX_INTELLIGENCE = 10
    MIN_AGILITY = 1
    MAX_AGILITY = 8
    MIN_LUCK = 1
    MAX_LUCK = 10

    def __init__(self):
        super(HalfMutantCharacter, self).__init__()

        self.strength = 5, {}
        self.perception = 5, {}
        self.endurance = 5, {}
        self.charisma = 5, {}
        self.intelligence = 5, {}
        self.agility = 5, {}
        self.luck = 5, {}

    def calculate_electricity_resistance(self):
        return 15

    def calculate_gas_resistance(self):
        return 0, 15

    def calculate_poison_resistance(self):
        return super().calculate_poison_resistance() + 10

    def calculate_radiation_resistance(self):
        return super().calculate_radiation_resistance() + 5

    def __str__(self):
        return "Half Mutant"


class DeathclawCharacter(FalloutCharacter):
    MIN_STRENGTH = 6
    MAX_STRENGTH = 14
    MIN_PERCEPTION = 4
    MAX_PERCEPTION = 12
    MIN_ENDURANCE = 1
    MAX_ENDURANCE = 13
    MIN_CHARISMA = 1
    MAX_CHARISMA = 3
    MIN_INTELLIGENCE = 1
    MAX_INTELLIGENCE = 4
    MIN_AGILITY = 6
    MAX_AGILITY = 16
    MIN_LUCK = 1
    MAX_LUCK = 10

    def __init__(self):
        super(DeathclawCharacter, self).__init__()

        self.strength = 8, {}
        self.perception = 7, {}
        self.endurance = 5, {}
        self.charisma = 1, {}
        self.intelligence = 1, {}
        self.agility = 9, {}
        self.luck = 4, {}

    def calculate_base_hit_points(self):
        return super().calculate_base_hit_points() + 15

    def calculate_melee_damage(self):
        return super().calculate_melee_damage() + 5

    def calculate_electricity_resistance(self):
        return 20

    def calculate_gas_resistance(self):
        return 0, 30

    def __str__(self):
        return "Deathclaw"


class DogCharacter(FalloutCharacter):
    MIN_STRENGTH = 1
    MAX_STRENGTH = 7
    MIN_PERCEPTION = 4
    MAX_PERCEPTION = 14
    MIN_ENDURANCE = 1
    MAX_ENDURANCE = 6
    MIN_CHARISMA = 1
    MAX_CHARISMA = 5
    MIN_INTELLIGENCE = 1
    MAX_INTELLIGENCE = 3
    MIN_AGILITY = 1
    MAX_AGILITY = 15
    MIN_LUCK = 1
    MAX_LUCK = 10

    def __init__(self):
        super(DogCharacter, self).__init__()

        self.strength = 3, {}
        self.perception = 7, {}
        self.endurance = 3, {}
        self.charisma = 3, {}
        self.intelligence = 2, {}
        self.agility = 7, {}
        self.luck = 5, {}

    def calculate_base_hit_points(self):
        return super().calculate_base_hit_points() - 7

    def calculate_carry_weight(self):
        return 0

    def calculate_electricity_resistance(self):
        return 10

    def __str__(self):
        return "Dog"


class RobotCharacter(FalloutCharacter):
    MIN_STRENGTH = 7
    MAX_STRENGTH = 12
    MIN_PERCEPTION = 7
    MAX_PERCEPTION = 12
    MIN_ENDURANCE = 7
    MAX_ENDURANCE = 12
    MIN_CHARISMA = 1
    MAX_CHARISMA = 1
    MIN_INTELLIGENCE = 12
    MAX_INTELLIGENCE = 10
    MIN_AGILITY = 1
    MAX_AGILITY = 12
    MIN_LUCK = 5
    MAX_LUCK = 5

    def __init__(self):
        super(RobotCharacter, self).__init__()

        self.strength = 7, {}
        self.perception = 7, {}
        self.endurance = 7, {}
        self.charisma = 1, {}
        self.intelligence = 5, {}
        self.agility = 5, {}
        self.luck = 5, {}

    def __str__(self):
        return "Robot"

    def calculate_base_hit_points(self):
        return super().calculate_base_hit_points() - 15

    def calculate_electricity_resistance(self):
        return -50

    def calculate_gas_resistance(self):
        return math.inf, math.inf

    def calculate_poison_resistance(self):
        return math.inf

    def calculate_radiation_resistance(self):
        return math.inf
