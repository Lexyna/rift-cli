from math import floor
import time

import click
from rift_cli.commands.buildings.building import buildings
from rift_cli.commands.generic.init import init
from rift_cli.commands.generic.status import status
from rift_cli.commands.planets.planets import planets
from rift_cli.data.game.gamedata import GameData
from rift_cli.display.console import console
from rift_cli.functions.generic.game import load_game, save_game, tick

@click.group
def cli():
    game: GameData = load_game()
    
    curr_time: float = time.time()
    delta_time: float = curr_time - game.last_update

    compounded_ticks: int = floor(delta_time/game.options.tickrate)
    console.log(f"{compounded_ticks} tick passed since last update")

    if compounded_ticks > 0 and not game.options.paused:    
        tick(game, compounded_ticks)
        game.current_tick += compounded_ticks
        game.last_update = curr_time
        save_game(game)
    pass

cli.add_command(init)
cli.add_command(status)
cli.add_command(planets)
cli.add_command(buildings)

if __name__ == '__main__':
    cli()