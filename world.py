from region import Region
from civilization import Civilization
import random
from events.event_manager import EventManager
from diplomacy.alliances import forge_random_alliances
from culture.global_culture import GlobalCulture
from eras.era_manager import EraManager
from religion.religion_manager import ReligionManager

class World:
    def __init__(self, width, height, civilization_count):
        self.width = width
        self.height = height
        self.grid = [[Region(x, y) for y in range(height)] for x in range(width)]
        self.civilizations = []
        self.event_manager = EventManager()
        self.global_culture = GlobalCulture()
        self.era_manager = EraManager()
        self.religion_manager = ReligionManager()
        self._populate(civilization_count)

    def _populate(self, count):
        positions = random.sample(
            [(x, y) for x in range(self.width) for y in range(self.height)],
            count
        )
        for pos in positions:
            region = self.grid[pos[0]][pos[1]]
            civ = Civilization(region)
            self.civilizations.append(civ)
            region.civilization = civ

    def display_state(self):
        for row in self.grid:
            line = ""
            for region in row:
                if region.civilization:
                    line += region.civilization.symbol
                else:
                    line += "."
            print(line)

    def advance_turn(self):
        modifiers = self.era_manager.get_modifiers()

        for civ in self.civilizations[:]:
            expanded = self._expand_civilization(civ, modifiers)
            if expanded:
                civ.inactive_turns = 0
            else:
                civ.inactive_turns += 1

        self._handle_splintering(modifiers)
        self._handle_collapse(modifiers)
        self.event_manager.trigger_random_event(self)
        self._handle_diplomacy()

        self.global_culture.update(self.civilizations)
        self.global_culture.influence(self.civilizations, modifiers["culture_strength"])

        for civ in self.civilizations:
            self.religion_manager.maybe_fund_religion(civ)
        self.religion_manager.spread_religion(self.civilizations)
        self.religion_manager.update_dominant(self.civilizations)

        self.era_manager.advance()

    def _expand_civilization(self, civ, modifiers):
        frontier = []
        for region in civ.regions:
            neighbors = self._get_neighbors(region.x, region.y)
            for n in neighbors:
                if n.civilization is None or (n.civilization != civ and not civ.is_allied_with(n.civilization)):
                    frontier.append(n)

        random.shuffle(frontier)
        for target in frontier:
            base_rate = modifiers["expansion_rate"]
            if civ.personality == "expansiva":
                base_rate += 0.2
            if civ.personality == "defensiva":
                base_rate -= 0.1

            if random.random() > base_rate:
                continue

            if target.civilization is None:
                target.civilization = civ
                civ.regions.append(target)
                civ.history.append(f"Se expande hacia la región ({target.x}, {target.y}).")
                return True
            elif target.civilization != civ:
                defender = target.civilization
                if civ.is_allied_with(defender) and civ.personality != "agresiva":
                    continue
                success = random.random() < 0.5
                if success:
                    defender.regions.remove(target)
                    target.civilization = civ
                    civ.regions.append(target)
                    civ.history.append(f"Conquista región ({target.x}, {target.y}) de {defender.name}.")
                    defender.history.append(f"Pierde región ({target.x}, {target.y}) ante {civ.name}.")
                    return True
                else:
                    civ.history.append(f"Intento fallido de conquista en ({target.x}, {target.y}) contra {defender.name}.")
                    return False
        return False

    def _handle_splintering(self, modifiers):
        candidates = [c for c in self.civilizations if len(c.regions) > 10]
        for civ in candidates:
            chance = modifiers["splinter_chance"]
            if civ.personality == "aislada":
                chance += 0.1
            if random.random() < chance:
                self._splinter_civilization(civ)

    def _splinter_civilization(self, civ):
        splinter_regions = random.sample(civ.regions[1:], k=min(3, len(civ.regions) - 1))
        for region in splinter_regions:
            civ.regions.remove(region)

        new_civ = Civilization(splinter_regions[0])
        new_civ.regions = splinter_regions
        for region in splinter_regions:
            region.civilization = new_civ

        civ.history.append(f"Escisión: una parte del pueblo se separa y forma la civilización {new_civ.name}.")
        new_civ.history.append(f"Surge como escisión de {civ.name}, trayendo consigo nuevas esperanzas.")
        self.civilizations.append(new_civ)

    def _handle_collapse(self, modifiers):
        for civ in self.civilizations[:]:
            chance = modifiers["collapse_chance"]
            if civ.personality == "defensiva":
                chance -= 0.05
            if len(civ.regions) <= 2 and civ.inactive_turns >= 3 and random.random() < chance:
                self._collapse_civilization(civ)

    def _collapse_civilization(self, civ):
        for region in civ.regions:
            region.civilization = None
        civ.history.append(f"La civilización {civ.name} colapsa tras años de decadencia.")
        self.civilizations.remove(civ)

    def _handle_diplomacy(self):
        for civ in self.civilizations:
            if civ.personality in ["diplomática", "defensiva"]:
                others = [c for c in self.civilizations if c != civ and not civ.is_allied_with(c)]
                if others:
                    partner = random.choice(others)
                    civ.form_alliance(partner)

    def _get_neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append(self.grid[nx][ny])
        return neighbors
