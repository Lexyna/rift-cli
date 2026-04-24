import datetime
from math import floor
import time

from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from rift_cli.display.formatter import number_to_roman
from rift_cli.functions.generic.game import load_game, save_game
from rift_cli.display.console import console
from rift_cli.utils.colors import color
from rift_cli.data.game.gamedata import game_ctx
import click
from rich.text import Text

@click.command
@game_ctx
def status(game: GameData) -> None:
        
    if game.options.paused:
        console.log(Text(f"Paused"))
        print_resources(game)
        game.last_update = time.time()
        save_game(game)
        return

    time_string = datetime.timedelta(seconds=game.current_tick*game.options.tickrate)

    msg_status = Text(f"Ticks since game started: ")
    msg_status.append(f"{game.current_tick} ({time_string})", f"bold {color.green}")
    console.log(msg_status)

    print_resources(game)

    pass

def print_resources(game: GameData) -> None:

    for res in game.resources.values():
        console.log(f"{res.grade.format()} {res.type.format()}({number_to_roman(res.lv)}): {res.amount}")

    pass