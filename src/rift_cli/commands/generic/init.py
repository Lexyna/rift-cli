from rift_cli.data.resources import Resource
from rift_cli.functions.generic.resource_utils import player_add_resource
from rift_cli.utils.colors import color
from rift_cli.display.console import console
from rift_cli.functions.generic.game import create_new_game_state, save_game
from rift_cli.utils.vars import RIFT_FOLDER, STATE_PATH
import click
import os
import shutil
from rich.text import Text

@click.command
@click.option("--ticks", "-t", type=int, default=10,
              help="Inits the game with <number> seconds per tick")
@click.option("--paused", "-p", is_flag=True, default=False,
              help="Startes the game in paused mode")
def init(ticks, paused):
    
    if os.path.isdir(RIFT_FOLDER):
        if not click.confirm("rift state found. Generate new State and delete old one?"):
            msg_aborted = Text("Aborted!")
            msg_aborted.stylize(f"{color.red}")
            console.print(msg_aborted)
            return
        else:
            shutil.rmtree(".rift-cli")
    click.echo("Creating new state")
    os.mkdir(RIFT_FOLDER)
    
    game_state = create_new_game_state(ticks, paused)

    save_game(game_state)

    msg_finished = Text(f"Created new game with {ticks}s/ticks")
    msg_finished.stylize(f"bold {color.green}")

    if paused:
        msg_finished.append("\nGame paused at tick 0", style=f"bold {color.yellow}")

    console.print(msg_finished)
    pass
