
from attr import dataclass


@dataclass
class Cost:
    metal: int = 0
    mineral: int = 0
    crystaks: int = 0
    liquid: int = 0
    organic: int = 0
    gas: int = 0

