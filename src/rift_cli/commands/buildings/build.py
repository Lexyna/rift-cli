from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.resources.metal_mine import MetalMine
from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.display.console import console
from rift_cli.utils.vars import BUILDING
from rift_cli.data.buildings.building_registry import registry_building_create
import click

@click.command
@game_ctx
@click.argument("name")
@click.argument("planet_id")
def build(game: GameData, name: str, planet_id: str) -> None:
    
    match name:
        case BUILDING.METALMINE: create_new_building(game, MetalMine(), planet_id)
        case _: console.log("No building '{name}' found", f"bold")
    pass

def create_new_building(game: GameData, building: Building, planet_id: str) -> None:
    #just add the building for now
    # move this to another function later and  create a detailed log

    if not planet_id in game.planets:
        console.log(f"No planets with id '{planet_id}' found")
        return
    
    if len(game.planets[planet_id].slots) >= game.planets[planet_id].max_slots:
        console.log("No available slot on this planet")
        return

    # add building
    game.planets[planet_id].slots.append(building.id)
    building.planet_id = planet_id
    game.buildings[building.id] = building

    if building.name in registry_building_create:
        registry_building_create[building.name](building, game)

    console.log(f"Added new building '{building.name}' on planet '{game.planets[planet_id].name}'")    
    pass