from rift_cli.data.buildings.building import Building
from rift_cli.data.game.optiondata import OptionData
from rift_cli.data.planetdata import PlanetData
from dataclasses import dataclass, field

from rift_cli.data.resources import ResourceType

@dataclass
class GameData:
    options: OptionData
    current_tick: int = 0
    resources: dict[ResourceType, int] = field(
        default_factory=lambda: {r: 0 for r in ResourceType})
    planets: dict[str, PlanetData] = field(default_factory=dict)
    buildings: dict[str, Building] = field(default_factory=dict)
    