from typing import Callable
from rift_cli.data.planetdata import PlanetData
from rift_cli.functions.generic.generators import generate_id
from dataclasses import dataclass, field

@dataclass
class Building:
    id: str = field(default_factory=lambda: generate_id(), init=False)
    name: str = "BaseBuilding"
    level: int = 1
    planet: str = "None"