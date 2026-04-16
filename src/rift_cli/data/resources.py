from dataclasses import dataclass
from enum import Enum

class ResouceType(Enum):
    METAL = 1

@dataclass
class Deposit:
    type: ResouceType
    amount: int

