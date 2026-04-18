from dataclasses import dataclass
from enum import Enum

class ResourceType(Enum):
    METAL = "metal"

@dataclass
class Deposit:
    type: ResourceType
    amount: int

