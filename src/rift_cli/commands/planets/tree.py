from rich.tree import Tree
from rich.columns import Columns

from rift_cli.data.game.gamedata import GameData, game_ctx
import click

from rift_cli.display.console import console

@click.command
@game_ctx
def tree(game: GameData) -> None:
    
    tree_list: list[Tree] = []

    for p in game.planets.values():
        planet_tree = Tree(p.name + f" ({len(p.slots)}/{p.max_slots})")
        for id in p.slots:
            if id in game.buildings:
                planet_tree.add(game.buildings[id].name + f" (lv.{game.buildings[id].level})")
        tree_list.append(planet_tree)
    
    coloumns = Columns(tree_list)
    console.log(coloumns)

    pass