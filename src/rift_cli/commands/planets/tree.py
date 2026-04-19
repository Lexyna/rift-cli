from rich.tree import Tree

from rift_cli.data.game.gamedata import GameData, game_ctx
import click

from rift_cli.display.console import console

@click.command
@game_ctx
def tree(game: GameData) -> None:
    
    tree = Tree("System")

    for p in game.planets.values():
        branch = tree.add(p.name + f" ({len(p.slots)}/{p.max_slots})")
        for id in p.slots:
            if id in game.buildings:
                branch.add(game.buildings[id].name)
    
    console.log(tree)

    pass