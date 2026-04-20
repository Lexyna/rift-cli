from asyncio import sleep
import time

from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.style import Style
from rich.text import Text

from rift_cli.data.buildings.building import Building
from rift_cli.data.buildings.building_registry import registry_display_building, registry_display_live_building
from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.display.console import console
import click

from rift_cli.utils.colors import color

@click.command
@game_ctx
@click.option("--live", "-l", is_flag=True, default=False,
              help="Displays live progress of buildings")
def status(game, live) -> None:

    if live:
        progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style=f"{color.green}"),
            TextColumn(text_format="[blue]{task.fields[desc]}"),
            "[magenta]{task.completed}/{task.total} seconds",
            refresh_per_second=2
        )

        for key in game.buildings.keys():
            building: Building = game.buildings[key]
            registry_display_live_building[building.name](progress, building, game, 0)

        try:
            progress.start()

            while not progress.finished:
                for task in progress.tasks:
                    progress.update(task.id, advance=1)
                    if task.finished:
                        progress.reset(task.id)
                time.sleep(1)
        finally:
            progress.stop()

        return

    for key in game.buildings.keys():
        building: Building = game.buildings[key]
        registry_display_building[building.name](building, game, 0)

    pass