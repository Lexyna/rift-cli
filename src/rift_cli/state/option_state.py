from dataclasses import dataclass

@dataclass
class option_state:
    tickrate: int = 10
    paused: bool = False