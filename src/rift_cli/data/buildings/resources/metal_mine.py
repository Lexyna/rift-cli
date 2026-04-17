from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.building_registry import building_tick
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from dataclasses import dataclass, field

from rift_cli.data.planetdata import PlanetData
from rift_cli.utils.vars import BUILDING

@dataclass
class MetalMine(Building):
    name: str = BUILDING.METALMINE
    
@building_tick(BUILDING.METALMINE)
def metal_mine_tick(building :Building, planet: PlanetData, game: GameData) -> None:
    # simple logic for now
    if planet.deposits[ResourceType.METAL] > 10:
        game.resources[ResourceType.METAL] += 10
    pass