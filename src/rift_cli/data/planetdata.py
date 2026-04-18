from dataclasses import dataclass, field
from rift_cli.data.resources import ResourceType

@dataclass
class PlanetData:
    id: str
    name: str
    max_slots: int 
    slots: list[str] = field(default_factory=list)
    deposits: dict[ResourceType, int] = field(
        default_factory=lambda: {r: 0 for r in ResourceType})
