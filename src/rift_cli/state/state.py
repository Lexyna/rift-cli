from rift_cli.state.option_state import OptionState
from rift_cli.data.planetdata import PlanetData
from dataclasses import dataclass, field

@dataclass
class State:
    options: OptionState
    current_tick: int = 0
    planets: list[PlanetData] = field(default_factory=list)