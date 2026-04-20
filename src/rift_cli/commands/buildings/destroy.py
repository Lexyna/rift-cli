from rift_cli.data.buildings.building import Building
from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.display.console import console
import click

@click.command
@game_ctx
@click.argument("id")
def destroy(game: GameData, id: str) -> None:
    
    console.log(f"try delete id: {id}")
    if id in game.buildings:
        building: Building = game.buildings[id]
        planet_id: str = building.planet_id

        if planet_id in game.planets:
            if id in game.planets[planet_id].slots:
                game.planets[planet_id].slots.remove(id)
        
        del game.buildings[id]
        console.log(f"Removed building: {building.id}")
    
    pass