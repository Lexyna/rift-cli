from rich.progress import Progress, Task, TaskID
from rich.text import Text

from rift_cli.data.buildings.building import Building, set_curr_tick
from rift_cli.data.buildings.building_registry import building_create, building_display, building_tick, building_display_live
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from rift_cli.display.console import console
from dataclasses import dataclass, field

from rift_cli.data.planetdata import PlanetData
from rift_cli.utils.colors import color
from rift_cli.utils.vars import BUILDING

@dataclass
class MetalMine(Building):
    name: str = BUILDING.METALMINE
    
@building_create(BUILDING.METALMINE)
def create(building: Building, game: GameData) -> None:
    console.log("Build new mine")
    pass

@building_tick(BUILDING.METALMINE)
def tick(building: Building, game: GameData, ticks: int) -> None:
    
    executed: int = set_curr_tick(building, ticks)
    
    if not building.planet_id in game.planets:
        return

    planet: PlanetData = game.planets[building.planet_id]

    # simple logic for now
    if planet.deposits[ResourceType.METAL] > 10 * executed:
        game.resources[ResourceType.METAL] += 10 * executed
        planet.deposits[ResourceType.METAL] -= 10 * executed
    pass

@building_display(BUILDING.METALMINE)
def display(building: Building, game: GameData, ticks: int) -> None:
    console.log(f"Metalmine({building.id}) ({building.level}) tick: {building.curr_tick}/{building.cooldown}")
    pass

@building_display_live(BUILDING.METALMINE)
def display_live(p: Progress, building: Building, game: GameData, ticks: int) -> TaskID:
    
    planetname = game.planets[building.planet_id].name
    name = Text(f"[{color.cyan}]{building.name}[/{color.cyan}]([{color.orange}]{planetname}[/{color.orange}])")

    task = p.add_task(name,
                    completed=building.curr_tick,
                    total=building.cooldown,
                    desc="Extracting: METAL")
    
    return task