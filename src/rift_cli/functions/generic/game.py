from rift_cli.state.state import state
from rift_cli.state.option_state import option_state
from rift_cli.utils.vars import STATE_PATH
import cattrs
import json
import os

def create_new_game_state(ticks: int, paused: bool) -> state:
    
    game_options: option_state = option_state(ticks, paused)

    game_state: state = state(options=game_options)

    return game_state

def load_game() -> state:
    with open(STATE_PATH, "r") as f:
        state_str: str = f.read()

    converter = cattrs.Converter()
    game_state: state =  converter.structure(json.loads(state_str), state)
    
    return game_state