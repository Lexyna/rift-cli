import time

from pydantic import BaseModel
from rift_cli.data.buildings.building_union import BUILDING_UNION
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.game.optiondata import OptionData
from rift_cli.data.planetdata import PlanetData
from rift_cli.data.resources import Resource
from rift_cli.utils.vars import RIFT_FOLDER, STATE_PATH
from rift_cli.data.buildings.building_registry import registry_building
from rift_cli.functions.planets.planet import create_planet
from rift_cli.display.console import console
import os

class GameSaveData(BaseModel):
    options: OptionData
    current_tick: int
    last_update: float
    credits: int
    resources: dict[str, Resource]
    planets: dict[str, PlanetData]
    buildings: dict[str, BUILDING_UNION]

def create_new_game_state(ticks: int, paused: bool) -> GameData:
    
    game_options: OptionData = OptionData(ticks, paused)

    game: GameData = GameData(options=game_options, 
                              current_tick=0, 
                              last_update=time.time(),
                              credits=1000, 
                              buildings={}, 
                              planets={}, 
                              resources={})

    game.last_update = time.time()

    for i in range(10):
        planet = create_planet()
        game.planets[planet.id] = planet

    return game

def load_game() -> GameData:
    with open(STATE_PATH, "r") as f:
        state_str: str = f.read()

    game_save: GameSaveData = GameSaveData.model_validate_json(state_str)

    game_state: GameData = GameData(
        options=game_save.options,
        current_tick=game_save.current_tick,
        last_update=game_save.last_update,
        credits=game_save.credits,
        resources=game_save.resources,
        planets=game_save.planets,
        buildings=game_save.buildings
    )

    return game_state

def save_game(game: GameData) -> None:

    if not os.path.isdir(RIFT_FOLDER):
        console.log(f"Failed to save game, no '{RIFT_FOLDER}' found.")
        return

    game_save_struct: GameSaveData = GameSaveData(
        options=game.options,
        current_tick=game.current_tick,
        last_update=game.last_update,
        credits=game.credits,
        resources=game.resources,
        planets=game.planets,
        buildings=game.buildings
    )

    with open(STATE_PATH, "w") as f:
        f.write(game_save_struct.model_dump_json())

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