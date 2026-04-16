from rift_cli.data.game.gamedata import GameData
from rift_cli.data.game.optiondata import OptionData
from rift_cli.utils.vars import STATE_PATH
from rift_cli.functions.planets.planet import create_planet
import cattrs
import json
import os

def create_new_game_state(ticks: int, paused: bool) -> GameData:
    
    game_options: OptionData = OptionData(ticks, paused)

    game_state: GameData = GameData(options=game_options)

    game_state.planets.append(create_planet())

    return game_state

def load_game() -> GameData:
    with open(STATE_PATH, "r") as f:
        state_str: str = f.read()

    converter = cattrs.Converter()
    game_state: GameData =  converter.structure(json.loads(state_str), GameData)
    
    return game_state