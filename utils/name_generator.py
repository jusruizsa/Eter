import random

def generate_name():
    prefixes = ["Ar", "Bel", "Kor", "Lum", "Zan"]
    suffixes = ["dor", "via", "tan", "mir", "lon"]
    return random.choice(prefixes) + random.choice(suffixes)
