

from dataclasses import dataclass

from rift_cli.data.buildings.building_registry import building_create
from rift_cli.data.planetdata import PlanetData
from rift_cli.data.resources import ResourceType
from rift_cli.display.console import console
from rift_cli.data.buildings.building import Building, set_curr_tick
from rift_cli.data.game.gamedata import GameData
from rift_cli.functions.generic.resource_utils import player_add_resource
from rift_cli.utils.vars import BUILDING


@dataclass
class Crystalmine(Building):
    name: str = BUILDING.CRYSTALMINE

#@building_create(BUILDING.CRYSTALMINE)
def create(building: Building, game: GameData) -> None:
    console.log("Build new crystal mine")
    pass

def tick(building: Building, game: GameData, ticks: int) -> None:
    
    executed: int = set_curr_tick(building, ticks)

    if not building.planet_id in game.planets:
        return
    
    planet: PlanetData = game.planets[building.planet_id]

    for deposit in planet.deposits:
        if deposit.extraction_diff <= 1 and deposit.resource.type == ResourceType.CRYSTAL:
            if deposit.resource.amount > 10 * executed:
                player_add_resource(game, deposit.resource, 10 * executed)
                deposit.resource.amount -= 10 * executed
    pass

