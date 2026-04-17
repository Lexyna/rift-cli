from rich.table import Table

from rift_cli.display.console import console
import click

from rift_cli.functions.generic.game import load_game

@click.command
def list() -> None:
    
    game = load_game()

    building_table = Table(title="buildings")
    building_table.box = None

    building_table.add_column("name")
    building_table.add_column("planet")
    building_table.add_column("id")

    for b in game.buildings.values():
        
        building_table.add_row(b.name,
                               b.planet,
                               b.id)
        pass

    console.log(building_table)

    pass