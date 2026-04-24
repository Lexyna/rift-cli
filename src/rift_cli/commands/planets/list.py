
from rich.table import Table

from rift_cli.data.game.gamedata import GameData, game_ctx
import click

from rift_cli.display.console import console
from rift_cli.utils.colors import color

@click.command
@game_ctx
def list(game: GameData) -> None:
    planet_table = Table(title="planets")
    planet_table.box = None

    planet_table.add_column("name")
    planet_table.add_column("id")
    planet_table.add_column("slots")
    planet_table.add_column("deposits")

    for p in game.planets.values():

        resources: str = ""
        for res in p.deposits:
            resources += f"[{res.resource.type.col}]" + res.resource.type.name + f"[/{res.resource.type.col}] "
        planet_table.add_row(f"[{color.yellow}]{p.name}",
                            f"[{color.cyan}]{p.id}",
                    f"{len(p.slots)}/{p.max_slots}",
                    resources)
        pass

    console.log(planet_table)
    pass