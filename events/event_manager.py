import random
from .event_types import ProsperityEvent, RebellionEvent, DisasterEvent, MiracleEvent

class EventManager:
    def __init__(self):
        self.event_classes = [ProsperityEvent, RebellionEvent, DisasterEvent, MiracleEvent]

    def trigger_random_event(self, world):
        if not world.civilizations:
            return
        event_cls = random.choice(self.event_classes)
        event = event_cls()
        target_civ = random.choice(world.civilizations)
        event.apply(target_civ, world)
