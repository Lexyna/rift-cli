from rift_cli.state.option_state import option_state
from dataclasses import dataclass

@dataclass
class state:
    options: option_state
    current_tick: int = 0