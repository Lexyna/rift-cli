from math import floor
import time

import click
from rich.text import Text

from rift_cli.data.game.gamedata import GameData
from rift_cli.data.game.optiondata import OptionData
from rift_cli.data.resources import Resource, resource_to_key
from rift_cli.utils.colors import color
from rift_cli.utils.vars import RIFT_FOLDER, STATE_PATH
from rift_cli.data.buildings.building_registry import registry_building
from rift_cli.functions.planets.planet import create_planet
from rift_cli.display.console import console
import datetime
import cattrs
import json
import os

def create_new_game_state(ticks: int, paused: bool) -> GameData:
    
    game_options: OptionData = OptionData(ticks, paused)

    game: GameData = GameData(options=game_options)

    game.last_update = time.time()

    for i in range(10):
        planet = create_planet()
        game.planets[planet.id] = planet

    return game

def load_game() -> GameData:
    with open(STATE_PATH, "r") as f:
        state_str: str = f.read()

    converter = cattrs.Converter()
    game_state: GameData =  converter.structure(json.loads(state_str), GameData)
    
    return game_state

def save_game(game: GameData) -> None:

    if not os.path.isdir(RIFT_FOLDER):
        console.log(f"Failed to save game, no '{RIFT_FOLDER}' found.")
        return

    converter = cattrs.Converter()
    with open(STATE_PATH, "w") as f:
        f.write(json.dumps(converter.unstructure(game)))

    return

def tick(game: GameData, ticks: int) -> None:
    for planet in game.planets.values():
        for building_id in planet.slots:
            if not building_id in game.buildings:
                continue
            building = game.buildings[building_id]
            registry_building[building.name](building, game, ticks)
            pass

    return

def player_add_resource(game: GameData, res: Resource, amount: int) -> None:
    key = resource_to_key(res)
    if not key in game.resources:
        game.resources[key] = res
        res.amount = 0
    game.resources[key].amount += amount
    pass