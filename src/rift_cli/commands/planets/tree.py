from rich.tree import Tree
from rich.columns import Columns

from rift_cli.data.game.gamedata import GameData, game_ctx
import click

from rift_cli.data.resources import Grade, Resource, print_resource
from rift_cli.display.console import console

@click.command
@game_ctx
def tree(game: GameData) -> None:
    
    tree_list: list[Tree] = []

    for p in game.planets.values():
        planet_tree = Tree(p.name + f" ({len(p.slots)}/{p.max_slots})")

        building_branch = planet_tree.add("buildings")
        for id in p.slots:
            if id in game.buildings:
                building_branch.add(game.buildings[id].get_name() + f" (lv.{game.buildings[id].level})")
        tree_list.append(planet_tree)

        resource_brnach = planet_tree.add("Resources")
        for value in p.deposits:
            res = value.resource
            resource_brnach.add(print_resource(res))

    
    coloumns = Columns(tree_list)
    console.log(coloumns)

    pass