from rift_cli.data.game.optiondata import OptionData
from rift_cli.data.planetdata import PlanetData
from dataclasses import dataclass, field

@dataclass
class GameData:
    options: OptionData
    current_tick: int = 0
    planets: list[PlanetData] = field(default_factory=list)