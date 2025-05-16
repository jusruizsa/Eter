from abc import ABC, abstractmethod

class BaseEvent(ABC):
    @abstractmethod
    def apply(self, civilization, world):
        pass
