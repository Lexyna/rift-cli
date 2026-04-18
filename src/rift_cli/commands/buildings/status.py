from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.building_registry import registry_display_building
from rift_cli.data.game.gamedata import GameData
from rift_cli.functions.generic.game import load_game
import click

@click.command
@click.option("--live", "-l", is_flag=True, default=False,
              help="Displays live progress of buildings")
def status(live) -> None:

    game: GameData = load_game()

    for key in game.buildings.keys():
        building: Building = game.buildings[key]
        registry_display_building[building.name](building, game, 0)

    pass