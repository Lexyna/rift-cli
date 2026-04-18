from math import floor
import time

from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import ResourceType
from rift_cli.functions.generic.game import load_game, save_game, tick
from rift_cli.display.console import console
from rift_cli.utils.colors import color
from rift_cli.functions.generic.generators import generate_planet_name
from rift_cli.display.formatter import format_number
import click
from rich.text import Text

@click.command
def status() -> None:
    
    game: GameData = load_game()
    
    if game.options.paused:
        console.log(Text(f"Paused"))
        print_resources(game)
        game.last_update = curr_time
        save_game(game)
        return

    msg_status = Text(f"Ticks since game started: ")
    msg_status.append(f"{game.current_tick}", f"bold {color.green}")
    console.log(msg_status)

    curr_time: float = time.time()
    delta_time: float = curr_time - game.last_update

    compounded_ticks: int = floor(delta_time/game.options.tickrate)
    console.log(f"{compounded_ticks} tick passed since last update")

    if compounded_ticks > 0:    
        tick(game, compounded_ticks)
        game.current_tick += compounded_ticks
        game.last_update = curr_time
        save_game(game)

    print_resources(game)

    pass

def print_resources(game: GameData) -> None:
    
    msg_resources = Text("Metal: ")
    msg_resources.append(f"{game.resources[ResourceType.METAL]}", f"bold {color.green}")
    console.log(msg_resources)

    pass