from rift_cli.data.game.gamedata import game_ctx, GameData
from rift_cli.commands.planets.list import list
from rift_cli.commands.planets.tree import tree
import click

@click.group
def planets() -> None:
    pass

planets.add_command(list)
planets.add_command(tree)