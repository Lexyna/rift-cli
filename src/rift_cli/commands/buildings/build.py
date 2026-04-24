from pickle import BUILD

from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.resources.mine import Mine
from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.data.planetdata import PlanetData
from rift_cli.data.resources import ResourceType
from rift_cli.display.console import console
from rift_cli.utils.vars import BUILDING_ID
from rift_cli.data.buildings.building_registry import registry_building_create
import click

@click.command
@game_ctx
@click.argument("name")
@click.argument("planet_id")
def build(game: GameData, name: str, planet_id: str) -> None:
    
    match name:
        case BUILDING_ID.METALMINE: create_new_building(game, Mine(extract=ResourceType.METAL), planet_id)
        case BUILDING_ID.MINERALMINE: create_new_building(game, Mine(extract=ResourceType.MINERAL), planet_id)
        case BUILDING_ID.CRYSTALMINE: create_new_building(game, Mine(extract=ResourceType.CRYSTAL), planet_id)        
        case BUILDING_ID.GASSIPHON: create_new_building(game, Mine(extract=ResourceType.GAS), planet_id)        
        case BUILDING_ID.HARVESTER: create_new_building(game, Mine(extract=ResourceType.ORGANIC), planet_id)        
        case BUILDING_ID.COLLECTOR: create_new_building(game, Mine(extract=ResourceType.LIQUID), planet_id)        
        case _: console.log(f"No building '{name}' found", f"bold")
    pass

def create_new_building(game: GameData, building: Building, planet_id: str) -> None:
    #just add the building for now
    # move this to another function later and  create a detailed log

    if not planet_id in game.planets:
        console.log(f"No planets with id '{planet_id}' found")
        return
    
    planet : PlanetData = game.planets[planet_id]

    if len(planet.slots) >= planet.max_slots:
        console.log("No available slot on this planet")
        return


    # add building
    game.planets[planet_id].slots.append(building.id)
    building.planet_id = planet_id
    game.buildings[building.id] = building

    if building.name in registry_building_create:
        registry_building_create[building.name](building, game)

    console.log(f"Added new building '{building.name}({building.id})' on planet '{game.planets[planet_id].name}'")    
    pass