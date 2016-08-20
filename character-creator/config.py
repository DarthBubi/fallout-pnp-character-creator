from character import Trait, Perk

__author__ = "Johannes Hackbarth"

ALL_RACES = {"Deathclaw", "Dog", "Ghoul", "Half Mutant", "Human", "Robot", "Super Mutant"}
ANIMALS = {"Deathclaw", "Dog"}
ROBOTS = {"Robot"}

TRAIT_LIST = [
    Trait("Fast Metabolism",
          "Your metabolic rate is twice normal. This means that you are much less resistant"
          " to radiation and poison, but your body heals faster.You get a 2 point bonus to "
          "Healing Rate, but your Radiation and Poison Resistance start at 0% (racial "
          "modifiers are added later). Robots cannot choose this trait.",
          ALL_RACES - ROBOTS),
    Trait("Bruiser",
          "A little slower, but a little bigger. You may not hit as often, but they will feel it when you do! Your total action points are lowered, but your Strength is increased. You get a 2 point bonus to Strength, but loose 2 Action Points.",
          ALL_RACES),
    Trait("Small Frame", "", ALL_RACES),
    Trait("One Handed", "", ALL_RACES - ANIMALS),
    Trait("Finesse", "", ALL_RACES),
    Trait("Kamikaze", "", ALL_RACES),
    Trait("Heavy Handed", "", ALL_RACES),
    Trait("Fast Shot", "", ALL_RACES - ANIMALS),
    Trait("Bloody Mess", "", ALL_RACES),
    Trait("Jinxed", "", ALL_RACES),
    Trait("Good Natured", "", ALL_RACES - ANIMALS - ROBOTS),
    Trait("Chem Reliant", "", ALL_RACES - ROBOTS),
    Trait("Chem Resistant", "", ALL_RACES - ROBOTS),
    Trait("Night Person", "", ALL_RACES),
    Trait("Skilled", "", ALL_RACES - ANIMALS - ROBOTS),
    Trait("Gifted", "", ALL_RACES - ROBOTS),
    Trait("Sex Appeal", "", ["Human"]),
    Trait("Glowing One", "", ["Ghoul"]),
    Trait("Tech Wizard", "", ALL_RACES - ANIMALS),
    Trait("Fear the Reaper", "", ["Ghoul"]),
    Trait("Vat Skin", "", ["Half Mutant", "Super Mutant"]),
    Trait("Ham Fisted", "", ["Half Mutant", "Super Mutant"]),
    Trait("Domesticated", "", ANIMALS),
    Trait("Rabid", "", ANIMALS),
    Trait("Tight Nuts", "", ROBOTS),
    Trait("Targeting Computer", "", ROBOTS),
    Trait("EMP Shielding", "", ROBOTS),
    Trait("Beta Software", "", ROBOTS)
]

PERK_LIST = [
    # Perk("Foo", "Bar", "42")
]
