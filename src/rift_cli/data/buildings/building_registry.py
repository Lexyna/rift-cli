from typing import Callable

from rift_cli.data.buildings.building import Building
from rift_cli.data.game.gamedata import GameData
from rift_cli.data.planetdata import PlanetData


BuildingTick = Callable[[Building, PlanetData, GameData, int], None]

registry_building: dict[str, BuildingTick] = {}

def building_tick(name: str):
    def decorator(fn: BuildingTick) -> BuildingTick:
        registry_building[name] = fn
        return fn
    return decorator