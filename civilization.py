import uuid
import random
from utils.name_generator import generate_name
from utils.ideology_pool import random_ideology

class Civilization:
    def __init__(self, region):
        self.id = str(uuid.uuid4())[:8]
        self.name = generate_name()
        self.ideology = random_ideology()
        self.symbol = self.name[0].upper()
        self.regions = [region]
        self.history = [f"Nace la civilización {self.name}, que {self.ideology}."]
        self.allies = set()
        self.inactive_turns = 0
        self.personality = random.choice([
            "expansiva", "defensiva", "diplomática", "aislada", "agresiva"
        ])
        self.history.append(f"Su personalidad es '{self.personality}'.")
        self.religion = None

    def is_allied_with(self, other):
        return other.id in self.allies

    def form_alliance(self, other):
        self.allies.add(other.id)
        other.allies.add(self.id)
        self.history.append(f"Forma una alianza con {other.name}.")
        other.history.append(f"Forma una alianza con {self.name}.")
