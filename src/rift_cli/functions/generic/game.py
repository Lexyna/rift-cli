from rift_cli.data.game.gamedata import GameData
from rift_cli.data.game.optiondata import OptionData
from rift_cli.utils.vars import RIFT_FOLDER, STATE_PATH
from rift_cli.functions.planets.planet import create_planet
from rift_cli.display.console import console
import cattrs
import json
import os

def create_new_game_state(ticks: int, paused: bool) -> GameData:
    
    game_options: OptionData = OptionData(ticks, paused)

    game: GameData = GameData(options=game_options)

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