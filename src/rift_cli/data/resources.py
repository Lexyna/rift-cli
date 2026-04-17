from dataclasses import dataclass
from enum import Enum

class ResourceType(Enum):
    METAL = "1"

@dataclass
class Deposit:
    type: ResourceType
    amount: int

