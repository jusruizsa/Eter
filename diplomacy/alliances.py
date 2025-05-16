import random

def forge_random_alliances(civilizations, max_attempts=2):
    shuffled = civilizations[:]
    random.shuffle(shuffled)

    for civ in shuffled:
        attempts = 0
        while attempts < max_attempts:
            potential = random.choice(shuffled)
            if potential != civ and not civ.is_allied_with(potential):
                civ.form_alliance(potential)
                break
            attempts += 1
