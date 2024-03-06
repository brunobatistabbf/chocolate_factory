from __future__ import annotations
from abc import ABC, abstractmethod

class IEasterEggProduct(ABC):
    @abstractmethod
    def ShowInfo(self):
        pass