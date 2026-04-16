from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.resources.metal_mine import MetalMine
from rift_cli.data.game.gamedata import GameData
from rift_cli.display.console import console
from rift_cli.functions.generic.game import load_game
from rift_cli.utils.vars import BUILDING
import click

@click.command
@click.argument("name")
@click.argument("planet_id")
def build(name: str, planet_id: str) -> None:
    
    match name:
        case BUILDING.METALMINE: create_new_building(MetalMine(), planet_id)
        case _: console.log(f"No object '{name}' found")
    pass

def create_new_building(building: Building, id: str) -> None:
    #just add the building for now
    # move this to another function later and  create a detailed log

    game: GameData = load_game()

    #if not id in game.planets:
    #    console.log("No planets with id found")

    console.log("Create")
    pass