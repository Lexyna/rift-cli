from math import floor
from typing import Callable
from rift_cli.data.planetdata import PlanetData
from rift_cli.functions.generic.generators import generate_id
from dataclasses import dataclass, field

@dataclass
class Building:
    id: str = field(default_factory=lambda: generate_id(), init=False)
    name: str = "BaseBuilding"
    level: int = 1
    planet_id: str = "None"
    curr_tick: int = 0
    cooldown: int = 20

# Sets the current tick for the buidlings and returns the times it ticked
def set_curr_tick(building: Building, ticks: int) -> int:
  
    executed: int = floor(ticks/building.cooldown)

    remainder: int  = ticks % building.cooldown

    curr_tick: int = building.curr_tick + remainder

    if curr_tick > building.cooldown:
        curr_tick -= building.cooldown
        executed += 1        
    
    building.curr_tick = curr_tick
    return executed