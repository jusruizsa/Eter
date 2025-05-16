from collections import Counter
import random

class GlobalCulture:
    def __init__(self):
        self.dominant_ideology = None

    def update(self, civilizations):
        ideologies = [civ.ideology for civ in civilizations]
        if not ideologies:
            self.dominant_ideology = None
            return

        counts = Counter(ideologies)
        most_common = counts.most_common(1)[0][0]
        self.dominant_ideology = most_common

    def influence(self, civilizations, strength=0.1):
        for civ in civilizations:
            if civ.ideology != self.dominant_ideology:
                if random.random() < strength:
                    old = civ.ideology
                    civ.ideology = self.dominant_ideology
                    civ.history.append(f"Adopta la ideología dominante global: de '{old}' a '{civ.ideology}'.")
