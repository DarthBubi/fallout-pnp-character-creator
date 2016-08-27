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
          "A little slower, but a little bigger. You may not hit as often, but they will feel it when you do! "
          "Your total action points are lowered, but your Strength is increased. You get a 2 point bonus to Strength,"
          " but loose 2 Action Points.",
          ALL_RACES),
    Trait("Small Frame",
          "You are not quite as big as everyone else, but that never slowed you down. You can't carry as much, but you"
          " are more agile. You get a 1 point bonus to Agility, but your Carry Weight is only 15 lbs Y Strength.",
          ALL_RACES),
    Trait("One Handed",
          "One of your hands is very dominant. You excel with single-handed weapons, but two-handed weapons cause a"
          " problem. You have a 40% penalty to hit with two-handed weapons, but get a 20% bonus to hit with weapons "
          "that only require one hand. Animals cannot choose this trait.",
          ALL_RACES - ANIMALS),
    Trait("Finesse",
          "Your attacks show a lot of finesse. You don't do as much damage, but you cause more critical hits. All of "
          "your attacks lose 30% of their damage (after reductions are made for Damage Resistance, etc.) but you gain "
          "a 10%bonus to Critical Chance.",
          ALL_RACES),
    Trait("Kamikaze",
          "By not paying attention to any threats, you can act a lot faster in a turn. This lowers your Armor Class "
          "to just what you are wearing, but you sequence much faster in a combat turn. You have no natural Armor "
          "Class (Armor Class is therefore 0 regardless of Agility). You must wear armor to get an Armor Class.Your "
          "sequence gets a 5 point bonus.",
          ALL_RACES),
    Trait("Heavy Handed",
          "You swing harder, not better. Your attacks are very brutal, but lack finesse. You rarely cause a good "
          "critical hit, but you always do more melee damage. You get a 4 point bonus to Melee Damage, but your "
          "critical hits do 30% less damage, and are 30% less likely to cripple a limb or cause unconsciousness.",
          ALL_RACES),
    Trait("Fast Shot",
          "You don't have time for a targeted attack, because you attack faster than normal people. It costs you one "
          "less action point to use a weapon. You cannot perform targeted shots, but all weapons take one less action "
          "point to use. Note that the Fast Shot trait has no effect on HtH or Melee attacks. Animals cannot choose "
          "this trait.",
          ALL_RACES - ANIMALS),
    Trait("Bloody Mess",
          "By some strange twist of fate, people around you die violently. You always see the worst way a person can "
          "die. This does not mean you kill them any faster or slower, but when they do die, it will be dramatic. "
          "Just how dramatic is up to the Gamemaster.",
          ALL_RACES),
    Trait("Jinxed",
          "The good thing is that everyone around you has more critical failures in combat. The bad thing is: so do "
          "you! If you, a member of your party, or a non-player character have a failure in combat, there is a "
          "greater likelihood the failure will be upgraded (downgraded?) to a critical failure. Critical failures are "
          "bad: weapons explode, you may hit the wrong target, you could lose part of your turn, or any number of bad "
          "things. Failures are 50% more likely to become critical failures around the character or anyone else in "
          "combat.",
          ALL_RACES),
    Trait("Good Natured",
          "You studied less-combative skills as you were growing up. Your combat skills start at a lower level, but "
          "First Aid, Doctor, Speech, and Barter are substantially improved. Those skills get a 20% bonus. You get a "
          "10% penalty to starting combat skills (Small Guns, Big Guns, Energy Weapons, Unarmed, and Melee Weapons). "
          "This is a one-time bonus. Animals and robots cannot choose this trait.",
          ALL_RACES - ANIMALS - ROBOTS),
    Trait("Chem Reliant",
          "You are more easily addicted to chems. Your chance to be addicted is twice normal, but you recover in half "
          "the time from their ill effects. Robots cannot choose this trait.",
          ALL_RACES - ROBOTS),
    Trait("Chem Resistant",
          "Chems only effect you half as long as normal, but your chance to be addicted is only 50% the normal amount. "
          "Robots cannot choose this trait.",
          ALL_RACES - ROBOTS),
    Trait("Night Person",
          "As a night-time person, you are more awake when the sun goes down. Your Intelligence and Perception are "
          "improved at night but are dulled during the day. You get a 1 point penalty to these Statistics from 0601 "
          "to 1800, and a 1 point bonus to these Stats from 1801 to 0600. Robots cannot choose this trait. Note that "
          "the bonus cannot take IN and PE above the character’s racial maximum or below the character’s racial "
          "minimum.",
          ALL_RACES),
    Trait("Skilled",
          "Since you spend more time improving your skills than a normal person, you gain more skill points. The "
          "tradeoff is that you do not gain as many extra abilities. You will gain a perk at one level higher than "
          "normal. For example, if you normally gained a perk every 4 levels, you would now gain a perk every 5 "
          "levels. You will get an additional 5 skill points per new experience level, and a one-time bonus of +10% "
          "to your skills when you begin the game. Animals and robots cannot choose this trait.",
          ALL_RACES - ANIMALS - ROBOTS),
    Trait("Gifted",
          "You have more innate abilities than most, so you have not spent as much time honing your skills. Your "
          "statistics are better than the average person, but your skills are lacking. All Stats get a 1- point "
          "bonus, but all skills get a 10% penalty and you receive 5 less Skill Points per level. Robots cannot "
          "choose this trait.",
          ALL_RACES - ROBOTS),
    Trait("Sex Appeal",
          "This trait increases your chances of having a good reaction with members of the opposite sex. "
          "Unfortunately, this trait tends to annoy members of your sex. Jealous twits. When interacting with members "
          "of the opposite sex, you gain a 1 point bonus to Charisma for reactions only. When making Speech and Barter "
          "rolls, you gain a 40% bonus for each. When interacting with members of the same sex, you have a 1 point "
          "penalty to Charisma for reactions only and have a 40% penalty to both Speech and Barter rolls. Only humans "
          "can choose this trait.",
          ["Human"]),
    Trait("Glowing One",
          "Extreme radiation exposure has left you glowing in the dark. Your glow eliminates modifiers from light in "
          "combat for both you and your enemies. In addition, you gain a +50% bonus to Radiation Resistance, but "
          "everyone around you takes 10 rads per hour (see Radiation under Damage and Death, below). Only Ghouls "
          "can choose this trait.",
          ["Ghoul"]),
    Trait("Tech Wizard",
          "You spent your formative years hunched over a bench learning all about the way things work. The trouble "
          "is that you’ve ruined your eyes! You get a +15% bonus to Science, Repair, and Lockpick skills, but you "
          "lose 1 Perception. Deathclaws and Dogs cannot choose this trait.",
          ALL_RACES - ANIMALS),
    Trait("Fear the Reaper",
          "You have cheated death! You gain perks as if you were a human, but you are now on death’s short list. "
          "This means that once a month, you must roll against Luck or else drop dead. Only Ghouls can choose this "
          "trait.",
          ["Ghoul"]),
    Trait("Vat Skin",
          "Other people find you hideous to behold and disgusting to smell after your “dip” in the FEV vats. "
          "The good news is that you gain a +10 bonus to your Armor Class thanks to your extra-tough skin. The bad "
          "news is that everyone within ten hexes of your location, friend and foe, suffers a 1-point penalty to "
          "Perception (you are unaffected). Only Mutants can choose this trait.",
          ["Half Mutant", "Super Mutant"]),
    Trait("Ham Fisted",
          "Genetic engineering – or dumb luck – has endowed you with huge hands. You get a “free” tag skill in "
          "Unarmed, but you suffer a -20% penalty to Small Guns, First Aid, Doctor, Repair, Science, and Lockpick "
          "Skills (these numbers cannot go below 0%). Only Mutants can choose this trait.",
          ["Half Mutant", "Super Mutant"]),
    Trait("Domesticated",
          "You have undergone extensive house training and have developed an above average Intelligence. Your IN is "
          "raised by 1, and can even go above your racial maximum, but you get a –2 penalty to Melee Damage. Only "
          "Deathclaws and Dogs can choose this trait.",
          ANIMALS),
    Trait("Rabid",
          "You are a half-crazed, feral killing machine. You are not affected by crippled limbs (blindness still "
          "affects you normally), and every time you kill an opponent in combat, you get 5 more APs that round. "
          "Chems, including stimpaks, have no effect on you. Only Deathclaws and Dogs can choose this trait.",
          ANIMALS),
    Trait("Tight Nuts",
          "This robot was built to take the knocks. You get double the base Damage Resistance to any attack, but "
          "you gain only half the Hit Points back from repairs. Only Robots can choose this trait.",
          ROBOTS),
    Trait("Targeting Computer",
          "You have been programmed with an onboard targeting computer. All attacks cost 1 extra AP to perform, "
          "but you can always add +15% to your chance to-hit. Only Robots can choose this trait.",
          ROBOTS),
    Trait("EMP Shielding",
          "You have a dedicated EMP shielding system. It takes you 2 AP to move 1 hex because of your heavy "
          "equipment, but you have a 30% Resistance to all forms of EMP attack. Only Robots can choose this trait.",
          ROBOTS),
    Trait("Beta Software",
          "You have been equipped with an experimental operating system and peripherals. You get 1 extra Tag Skill, "
          "but whenever using ANY tag skill, you must roll against Luck or suffer an automatic failure and, in "
          "combat, a loss of all APs for that round. Only Robots can choose this trait.",
          ROBOTS)
]

PERK_LIST = [
    # Perk("Foo", "Bar", "42")
]
