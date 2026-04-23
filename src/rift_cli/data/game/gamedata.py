from rift_cli.data.buildings.building import Building
from rift_cli.data.game.optiondata import OptionData
from rift_cli.data.planetdata import PlanetData
from rift_cli.data.resources import Grade, Resource, ResourceType
from dataclasses import dataclass, field
import click

@dataclass
class GameData:
    options: OptionData
    current_tick: int = 0
    last_update: float = 0  #timestamp
    credits: int  = 1000
    resources: dict[str, Resource] = field(default_factory=dict)
    planets: dict[str, PlanetData] = field(default_factory=dict)
    buildings: dict[str, Building] = field(default_factory=dict)

game_ctx = click.make_pass_decorator(GameData, ensure=True)