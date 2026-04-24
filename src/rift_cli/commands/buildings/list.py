from rich.table import Table

from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.display.console import console
import click

from rift_cli.functions.generic.game import load_game
from rift_cli.utils.colors import color

@click.command
@game_ctx
def list(game: GameData) -> None:
    
    building_table = Table(title="buildings")
    building_table.box = None

    building_table.add_column("name")
    building_table.add_column("lv", justify="right")
    building_table.add_column("planet")
    building_table.add_column("id")

    for b in game.buildings.values():
        
        planet_name: str = game.planets[b.planet_id].name

        building_table.add_row(b.get_name(),
                               str(b.level),
                               f"[{color.orange}]{planet_name}[/{color.orange}]",
                               f"[{color.cyan}]{b.id}[/{color.cyan}]")
        pass

    console.log(building_table)

    pass