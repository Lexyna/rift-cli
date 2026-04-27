from math import floor

from pydantic import BaseModel

from rift_cli.data.cost.cost import Cost
from rift_cli.functions.generic.generators import generate_id
from dataclasses import dataclass, field

class Building(BaseModel):
    id: str = field(default=generate_id())
    name: str = "BaseBuilding"
    level: int = 1
    planet_id: str = "None"
    curr_tick: int = 0
    cooldown: int = 20
    _cost: Cost = Cost()

    def get_name(self) -> str:
        return ""

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