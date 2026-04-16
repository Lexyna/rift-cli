from dataclasses import dataclass, field
from rift_cli.data.resources import ResouceType

@dataclass
class PlanetData:
    id: str
    name: str
    max_slots: int 
    slots: list[str] = field(default_factory=list)
    deposits: list[ResouceType] = field(default_factory=list)
