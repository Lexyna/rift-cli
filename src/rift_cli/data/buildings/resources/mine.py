from email.policy import default
from typing import Literal

from rich.progress import Progress, TaskID
from rich.text import Text

from rift_cli.data.buildings.building import Building, set_curr_tick
from rift_cli.data.buildings.building_registry import building_create, building_display, building_tick, building_display_live
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from rift_cli.display.console import console

from rift_cli.data.planetdata import PlanetData
from rift_cli.functions.generic.resource_utils import player_add_resource
from rift_cli.utils.colors import color
from rift_cli.utils.vars import BUILDING_TYPE

class Mine(Building):
    type: Literal["mine"] = "mine"
    name: str = BUILDING_TYPE.MINE
    extract: ResourceType = ResourceType.METAL

    def get_name(self):
        match(self.extract):
            case ResourceType.GAS: return f"[{self.extract.col}]{self.extract.value}siphon[/{self.extract.col}]"
            case ResourceType.LIQUID: return f"[{self.extract.col}]{self.extract.value}collector[/{self.extract.col}]"
            case ResourceType.ORGANIC: return f"[{self.extract.col}]{self.extract.value}harvester[/{self.extract.col}]"
            case _: return f"[{self.extract.col}]{self.extract.value}mine[/{self.extract.col}]"

@building_create(BUILDING_TYPE.MINE)
def create(building: Mine, game: GameData) -> None:
    console.log(f"Build new  {building.extract.name} mine")
    pass

@building_tick(BUILDING_TYPE.MINE)
def tick(building: Mine, game: GameData, ticks: int) -> None:
    
    executed: int = set_curr_tick(building, ticks)
    
    if not building.planet_id in game.planets:
        return

    planet: PlanetData = game.planets[building.planet_id]

    for deposit in planet.deposits:
        if deposit.extraction_diff <= 1 and deposit.resource.type == building.extract:
            if deposit.resource.amount > 10 * executed:
                player_add_resource(game, deposit.resource, 10 * executed)
                deposit.resource.amount -= 10 * executed
    pass

@building_display(BUILDING_TYPE.MINE)
def display(building: Mine, game: GameData, ticks: int) -> None:
    console.log(f"[{building.extract.col}]{building.extract.name}mine({building.id}) [/{building.extract.col}] ({building.level}) tick: {building.curr_tick}/{building.cooldown}")
    pass

@building_display_live(BUILDING_TYPE.MINE)
def display_live(p: Progress, building: Mine, game: GameData, ticks: int) -> TaskID:
    
    planetname = game.planets[building.planet_id].name
    name = Text(f"[{color.cyan}]{building.name}[/{color.cyan}]([{color.orange}]{planetname}[/{color.orange}])")

    task = p.add_task(name,
                    completed=building.curr_tick * game.options.tickrate,
                    total=building.cooldown * game.options.tickrate,
                    desc=f"Extracting: {building.extract.format()}")
    
    return task