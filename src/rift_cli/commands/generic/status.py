from rift_cli.functions.generic.game import load_game
from rift_cli.state import state
from rift_cli.display.console import console
from rift_cli.utils.colors import color
from rift_cli.functions.generic.generators import generate_planet_name
import click
from rich.text import Text

@click.command
def status() -> None:
    
    game_state: state = load_game()
    
    msg_status = Text(f"Ticks since game started: ")
    msg_status.append(f"{game_state.current_tick}", f"bold {color.green}")

    console.log(msg_status)
    console.log(generate_planet_name())
    pass