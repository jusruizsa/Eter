import random

class EraManager:
    def __init__(self):
        self.era = "Edad Antigua"
        self.turn = 0

    def advance(self):
        self.turn += 1
        if self.turn % 10 == 0:
            self._next_era()

    def _next_era(self):
        eras = [
            "Edad Antigua",
            "Edad Media",
            "Edad Moderna",
            "Edad Dorada",
            "Edad Oscura"
        ]
        self.era = random.choice(eras)

    def get_modifiers(self):
        if self.era == "Edad Antigua":
            return {"expansion_rate": 1.0, "splinter_chance": 0.1, "culture_strength": 0.05, "collapse_chance": 0.05}
        elif self.era == "Edad Media":
            return {"expansion_rate": 0.6, "splinter_chance": 0.3, "culture_strength": 0.05, "collapse_chance": 0.1}
        elif self.era == "Edad Moderna":
            return {"expansion_rate": 0.8, "splinter_chance": 0.1, "culture_strength": 0.2, "collapse_chance": 0.05}
        elif self.era == "Edad Dorada":
            return {"expansion_rate": 1.5, "splinter_chance": 0.0, "culture_strength": 0.3, "collapse_chance": 0.01}
        elif self.era == "Edad Oscura":
            return {"expansion_rate": 0.3, "splinter_chance": 0.4, "culture_strength": 0.02, "collapse_chance": 0.3}
        return {}
