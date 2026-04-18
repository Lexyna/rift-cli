from rift_cli.data.buildings.building import Building, set_curr_tick
from rift_cli.data.buildings.building_registry import building_tick
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from rift_cli.display.console import console
from dataclasses import dataclass, field

from rift_cli.data.planetdata import PlanetData
from rift_cli.utils.vars import BUILDING

@dataclass
class MetalMine(Building):
    name: str = BUILDING.METALMINE
    
@building_tick(BUILDING.METALMINE)
def metal_mine_tick(building :Building, planet: PlanetData, game: GameData, ticks: int) -> None:
    
    executed: int = set_curr_tick(building, ticks)
    
    # simple logic for now
    if planet.deposits[ResourceType.METAL] > 10 * executed:
        game.resources[ResourceType.METAL] += 10 * executed
    console.log(f"Hello from the Mines! - {building.id} on {planet.name} - triggered: {executed} times, currtick: {building.curr_tick}")
    pass