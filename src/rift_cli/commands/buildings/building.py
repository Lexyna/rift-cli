from rift_cli.commands.buildings.build import build
from rift_cli.data.game.gamedata import GameData
from rift_cli.functions.generic.game import load_game
import click

@click.group
def buildings() -> None:
    pass

buildings.add_command(build)