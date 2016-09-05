import calc_skills

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
        self.strength = 0
        self.perception = 0
        self.endurance = 0
        self.charisma = 0
        self.intelligence = 0
        self.agility = 0
        self.luck = 0

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

        self.traits = []
        self.perks = []

    def calculate_base_skills(self):
        self.small_guns = calc_skills.calculate_small_guns(self.agility)
        self.big_guns = calc_skills.calculate_big_guns(self.strength, self.perception, self.endurance)
        self.energy_weapons = calc_skills.calculate_energy_weapons(self.perception, self.intelligence)
        self.unarmed = calc_skills.calculate_unarmed(self.agility, self.strength)
        self.melee_weapons = calc_skills.calculate_unarmed(self.agility, self.strength)
        self.throwing = calc_skills.calculate_throwing(self.agility)
        self.explosives = calc_skills.calculate_explosives(self.perception, self.luck)
        self.doctor = calc_skills.calculate_doctor(self.perception, self.endurance)
        self.sneak = calc_skills.calculate_sneak(self.agility)
        self.lockpick = calc_skills.calculate_lockpick(self.perception, self.agility)
        self.traps = calc_skills.caclulate_traps(self.perception, self.agility)
        self.science = calc_skills.calculate_science(self.intelligence)
        self.repair = calc_skills.calculate_repair(self.intelligence)
        self.pilot = calc_skills.calculate_pilot(self.agility, self.perception)
        self.speech = calc_skills.calculate_speech(self.charisma)
        self.barter = calc_skills.calculate_barter(self.charisma)
        self.gambling = calc_skills.calculate_gambling(self.perception, self.luck)
        self.survival = calc_skills.calculate_survival(self.endurance, self.intelligence)

    def calculate_base_hit_points(self):
        return 15 + self.strength + 2 * self.endurance

    def calculate_base_action_points(self):
        return int(self.agility/2 + 5)

    def calculate_carry_weight(self):
        return 25 + 25 * self.strength

    def calculate_melee_damage(self):
        return 1 if self.strength < 6 else self.strength - 5

    def add_trait(self, trait):
        if self.traits.__len__() < 2 and not self.traits.__contains__(trait):
            self.traits.append(trait)

    def remove_trait(self, trait):
        if self.traits.__contains__(trait):
            self.traits.remove(trait)

    def calculate_poison_resistance(self):
        return 5 * self.endurance

    def calculate_radiation_resistance(self):
        return 2 * self.endurance

    def calculate_gas_resistance(self):
        pass

    def calculate_electricity_resistance(self):
        pass

    def calculate_damage_resistance(self):
        return self.agility + self.perception

    def calculate_healing_rate(self):
        return int(self.endurance/3)


class Trait(object):

    def __init__(self, name, effect, races, attr_mod=0, skill_mod=0, misc_mod=0):
        self.name = name
        self.effect = effect
        self.races = races
        self.attribute_mod = attr_mod
        self.skill_mod = skill_mod
        self.misc_mod = misc_mod

    def __str__(self, *args, **kwargs):
        return self.name


class Perk(Trait):

    def __init__(self, name, effect, races, level=0, attr_mod=0, skill_mod=0, misc_mod=0):
        super(Perk, self).__init__(name, effect, races, attr_mod, skill_mod, misc_mod)
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

        self.strength = 5
        self.perception = 5
        self.endurance = 5
        self.charisma = 5
        self.intelligence = 5
        self.agility = 5
        self.luck = 5

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

        self.strength = 3
        self.perception = 8
        self.endurance = 5
        self.charisma = 4
        self.intelligence = 6
        self.agility = 4
        self.luck = 7

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

        self.strength = 8
        self.perception = 6
        self.endurance = 6
        self.charisma = 5
        self.intelligence = 5
        self.agility = 4
        self.luck = 5

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

        self.strength = 5
        self.perception = 5
        self.endurance = 5
        self.charisma = 5
        self.intelligence = 5
        self.agility = 5
        self.luck = 5

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

        self.strength = 8
        self.perception = 7
        self.endurance = 5
        self.charisma = 1
        self.intelligence = 1
        self.agility = 9
        self.luck = 4

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

        self.strength = 3
        self.perception = 7
        self.endurance = 3
        self.charisma = 3
        self.intelligence = 2
        self.agility = 7
        self.luck = 5

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

        self.strength = 7
        self.perception = 7
        self.endurance = 7
        self.charisma = 1
        self.intelligence = 5
        self.agility = 5
        self.luck = 5

    def __str__(self):
        return "Robot"
