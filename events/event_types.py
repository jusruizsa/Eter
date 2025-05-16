from .base_event import BaseEvent
import random

class ProsperityEvent(BaseEvent):
    def apply(self, civilization, world):
        expansion_count = 2
        possible_targets = []
        for region in civilization.regions:
            for neighbor in world._get_neighbors(region.x, region.y):
                if neighbor.civilization is None:
                    possible_targets.append(neighbor)
        random.shuffle(possible_targets)
        added = 0
        for target in possible_targets:
            if added >= expansion_count:
                break
            target.civilization = civilization
            civilization.regions.append(target)
            added += 1
        civilization.history.append(f"Una era de prosperidad permite expandirse a {added} regiones adicionales.")

class RebellionEvent(BaseEvent):
    def apply(self, civilization, world):
        if len(civilization.regions) <= 1:
            return
        lost_region = random.choice(civilization.regions[1:])
        civilization.regions.remove(lost_region)
        lost_region.civilization = None
        civilization.history.append(f"Una rebelión provoca la pérdida de la región ({lost_region.x}, {lost_region.y}).")

class DisasterEvent(BaseEvent):
    def apply(self, civilization, world):
        if not civilization.regions:
            return
        target = random.choice(civilization.regions)
        civilization.regions.remove(target)
        target.civilization = None
        civilization.history.append(f"Un desastre natural destruye la región ({target.x}, {target.y}).")

class MiracleEvent(BaseEvent):
    def apply(self, civilization, world):
        old_ideology = civilization.ideology
        from utils.ideology_pool import random_ideology
        new_ideology = random_ideology()
        while new_ideology == old_ideology:
            new_ideology = random_ideology()
        civilization.ideology = new_ideology
        civilization.history.append(f"Ocurre un milagro. Abandonan '{old_ideology}' y adoptan '{new_ideology}'.")
