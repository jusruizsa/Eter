import random
from collections import Counter

class ReligionManager:
    def __init__(self):
        self.religions = {}
        self.dominant_religion = None

    def maybe_fund_religion(self, civilization):
        if civilization.religion is not None:
            return
        if random.random() < 0.1:
            name = self._generate_religion_name()
            self.religions[name] = [civilization.id]
            civilization.religion = name
            civilization.history.append(f"Funda la religión '{name}'.")

    def spread_religion(self, civilizations):
        for civ in civilizations:
            if civ.religion is None:
                candidates = [c for c in civilizations if c.religion]
                if candidates:
                    spreader = random.choice(candidates)
                    if random.random() < 0.1:
                        civ.religion = spreader.religion
                        spreader.history.append(f"La religión '{spreader.religion}' se expande a {civ.name}.")
                        civ.history.append(f"Adopta la religión '{spreader.religion}'.")

    def update_dominant(self, civilizations):
        religions = [civ.religion for civ in civilizations if civ.religion]
        if religions:
            counts = Counter(religions)
            self.dominant_religion = counts.most_common(1)[0][0]
        else:
            self.dominant_religion = None

    def _generate_religion_name(self):
        prefixes = ["Sol", "Luz", "Som", "Voz", "Fe"]
        suffixes = ["aria", "ismo", "edra", "tismo", "nía"]
        return random.choice(prefixes) + random.choice(suffixes)
