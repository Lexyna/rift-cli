import datetime
from math import floor
import os
import time

import click
from rift_cli.commands.buildings.building import buildings
from rift_cli.commands.generic.init import init
from rift_cli.commands.generic.resources import resources
from rift_cli.commands.generic.status import status
from rift_cli.commands.generic.test import test
from rift_cli.commands.planets.planets import planets
from rift_cli.data.game.gamedata import GameData
from rift_cli.display.console import console
from rift_cli.functions.generic import game
from rift_cli.functions.generic.game import load_game, save_game, tick
from rift_cli.utils.vars import RIFT_FOLDER

@click.group
@click.pass_context
def cli(ctx: click.Context):
    
    # TODO: Add better check with route to init or aboard
    if not os.path.isdir(RIFT_FOLDER):
        return

    gamestate: GameData = load_game()

    game_ctx = gamestate
    ctx.obj = game_ctx
    
    curr_time: float = time.time()
    delta_time: float = curr_time - game_ctx.last_update

    compounded_ticks: int = floor(delta_time/game_ctx.options.tickrate)
    time_string = datetime.timedelta(seconds=compounded_ticks*game_ctx.options.tickrate)

    console.log(f"{compounded_ticks} ({time_string}) tick passed since last update")

    if compounded_ticks > 0 and not game_ctx.options.paused:    
        tick(game_ctx, compounded_ticks)
        game_ctx.current_tick += compounded_ticks
        game_ctx.last_update = curr_time
    
    ctx.call_on_close(lambda: save_game(game_ctx))
    pass

cli.add_command(init)
cli.add_command(status)
cli.add_command(resources)
cli.add_command(test)
cli.add_command(planets)
cli.add_command(buildings)

if __name__ == '__main__':
    cli()