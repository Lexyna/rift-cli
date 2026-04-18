from rift_cli.data.game.gamedata import game_ctx, GameData
from rift_cli.functions.generic.game import load_game
from rift_cli.display.console import console
from rich.table import Table
import click

@click.command
@game_ctx
def planets(game: GameData) -> None:
    
    planet_table = Table(title="planets")
    planet_table.box = None

    planet_table.add_column("name")
    planet_table.add_column("id")
    planet_table.add_column("slots")
    planet_table.add_column("deposits")

    for p in game.planets.values():

        resources: str = ""
        for key in p.deposits:
            resources += key.name + " "
        planet_table.add_row(p.name,
                            p.id,
                    f"{len(p.slots)}/{p.max_slots}",
                    resources)
        pass

    console.log(planet_table)

    pass