__author__ = "Johannes Hackbarth"


def calculate_small_guns(agility):
    return 5 + 4 * agility


def calculate_big_guns(strength, perception, endurance):
    return 10 + strength + perception + endurance


def calculate_energy_weapons(perception, intelligence):
    return 10 + perception + intelligence


def calculate_unarmed(agility, strength):
    return 30 + 2 * (agility + strength)


def calculate_melee_weapons(agility, strength):
    return 10 + 2 * (agility + strength)


def calculate_throwing(agility):
    return 4 * agility


def calculate_explosives(perception, luck):
    return 2 + 2 * perception + luck/2


def calculate_doctor(perception, endurance):
    return 5 + perception + endurance


def calculate_sneak(agility):
    return 5 + 3 * agility


def calculate_lockpick(perception, agility):
    return 10 + perception + agility


def caclulate_traps(perception, agility):
    return 10 + perception + agility


def calculate_science(intelligence):
    return 4 * intelligence


def calculate_repair(intelligence):
    return 3 * intelligence


def calculate_pilot(agility, perception):
    return 2 * (agility + perception)


def caclulate_speech(charisma):
    return 5 * charisma


def calculate_barter(charisma):
    return 4 * charisma


def calculate_gambling(perception, luck):
    return 2 * (perception + luck)


def calculate_survival(endurance, intelligence):
    return 2 * (endurance + intelligence)
