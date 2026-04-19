from dataclasses import dataclass
from enum import Enum

class ResourceType(Enum):
    METAL = "metal"
    CREDITS = "credits"

@dataclass
class Deposit:
    type: ResourceType
    amount: int

