from typing import Callable

from rich.progress import Progress, Task, TaskID

from rift_cli.data.buildings.building import Building
from rift_cli.data.game.gamedata import GameData

BuildingCreate = Callable[[Building, GameData], None]
BuildingDestroy = Callable[[Building, GameData], None]

BuildingTick = Callable[[Building, GameData, int], None]
BuildingDisplay = Callable[[Building, GameData, int], None]
BuildingDisplayLive = Callable[[Progress, Building, GameData, int], TaskID]

registry_building: dict[str, BuildingTick] = {}

registry_building_create: dict[str, BuildingCreate] = {}
registry_building_destroy: dict[str, BuildingDisplay] = {}

registry_display_building: dict[str, BuildingDisplay] = {}
registry_display_live_building: dict[str, BuildingDisplayLive] = {}

def building_create(name: str):
    def decorator(fn: BuildingCreate) -> BuildingCreate:
        registry_building_create[name] = fn
        return fn
    return decorator

def building_destroy(name: str):
    def decorator(fn: BuildingDestroy) -> BuildingDestroy:
        registry_building_destroy[name] = fn
        return fn
    return decorator


def building_tick(name: str):
    def decorator(fn: BuildingTick) -> BuildingTick:
        registry_building[name] = fn
        return fn
    return decorator

def building_display(name: str):
    def decorator(fn: BuildingDisplay) -> BuildingDisplay:
        registry_display_building[name] = fn
        return fn
    return decorator

def building_display_live(name: str):
    def decorator(fn: BuildingDisplayLive) -> BuildingDisplayLive:
        registry_display_live_building[name] = fn
        return fn
    return decorator