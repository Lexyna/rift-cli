from rift_cli.state.state import State
from rift_cli.state.option_state import OptionState
from rift_cli.utils.vars import STATE_PATH
from rift_cli.functions.planets.planet import create_planet
import cattrs
import json
import os

def create_new_game_state(ticks: int, paused: bool) -> State:
    
    game_options: OptionState = OptionState(ticks, paused)

    game_state: State = State(options=game_options)

    game_state.planets.append(create_planet())

    return game_state

def load_game() -> State:
    with open(STATE_PATH, "r") as f:
        state_str: str = f.read()

    converter = cattrs.Converter()
    game_state: State =  converter.structure(json.loads(state_str), State)
    
    return game_state